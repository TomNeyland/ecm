# Copyright (c) 2010-2011 Robin Jarry
# 
# This file is part of EVE Corporation Management.
# 
# EVE Corporation Management is free software: you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at your 
# option) any later version.
# 
# EVE Corporation Management is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for 
# more details.
# 
# You should have received a copy of the GNU General Public License along with 
# EVE Corporation Management. If not, see <http://www.gnu.org/licenses/>.

__date__ = "2010-12-25"

__author__ = "diabeteman"

import json
from datetime import datetime, timedelta

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.template.defaultfilters import pluralize
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.db import connection

from ecm.view.decorators import check_user_access
from ecm.view.assets import extract_divisions, HTML_ITEM_SPAN
from ecm.core.eve import constants, db
from ecm.core import utils
from ecm.data.assets.models import Asset, AssetDiff
from ecm.data.corp.models import Hangar
from ecm.view import getScanDate, DATE_PATTERN




#------------------------------------------------------------------------------
def last_date(request):
    # if called without date, redirect to the last date.
    since_weeks = int(request.GET.get("since_weeks", "8"))
    to_weeks = int(request.GET.get("to_weeks", "0"))
    oldest_date = datetime.now() - timedelta(weeks=since_weeks)
    newest_date = datetime.now() - timedelta(weeks=to_weeks)

    query = AssetDiff.objects.values_list("date", flat=True).distinct().order_by("-date")
    query = query.filter(date__gte=oldest_date)
    query = query.filter(date__lte=newest_date)
    
    try:
        last_date = query[0]
        date_str = datetime.strftime(last_date, DATE_PATTERN)
        return redirect("/assets/changes/%s?since_weeks=%d&to_weeks=%d" % (date_str, since_weeks, to_weeks))
    except IndexError:
        return render_to_response("assets/assets_no_data.html", context_instance=RequestContext(request))

#------------------------------------------------------------------------------
@check_user_access()
def root(request, date_str):
    
    all_hangars = Hangar.objects.all().order_by("hangarID")
    try: 
        divisions_str = request.GET["divisions"]
        divisions = [ int(div) for div in divisions_str.split(",") ]
        for h in all_hangars: 
            h.checked = h.hangarID in divisions
    except: 
        divisions, divisions_str = None, None
        for h in all_hangars: 
            h.checked = True
    
    show_in_space = json.loads(request.GET.get("space", "true"))
    show_in_stations = json.loads(request.GET.get("stations", "true"))
    
    since_weeks = int(request.GET.get("since_weeks", "8"))
    to_weeks = int(request.GET.get("to_weeks", "0"))
    
    oldest_date = datetime.now() - timedelta(weeks=since_weeks)
    newest_date = datetime.now() - timedelta(weeks=to_weeks)
    
    query = AssetDiff.objects.values_list("date", flat=True).distinct().order_by("-date")
    query = query.filter(date__gte=oldest_date)
    query = query.filter(date__lte=newest_date)
    
    dates = []
    for date in query:
        dates.append({ 
            "value" : datetime.strftime(date, DATE_PATTERN),
            "show" : utils.print_time_min(date)
        })

    data = { 'show_in_space' : show_in_space,
          'show_in_stations' : show_in_stations,
             'divisions_str' : divisions_str,
                   'hangars' : all_hangars,
                 'scan_date' : getScanDate(Asset),
               'since_weeks' : since_weeks,
                  'to_weeks' : to_weeks,
                  "date_str" : date_str,
                     'dates' : dates }

    try:
        date_asked = datetime.strptime(date_str, DATE_PATTERN)
        if AssetDiff.objects.filter(date=date_asked):
            return render_to_response("assets/assets_diff.html", data, RequestContext(request))
        else:
            return render_to_response("assets/assets_no_data.html", RequestContext(request))
    except:
        return redirect("/assets/changes")
    

#------------------------------------------------------------------------------
@check_user_access()
@cache_page(3 * 60 * 60) # 3 hours cache
def systems_data(request, date_str):
    date = datetime.strptime(date_str, DATE_PATTERN)
    divisions = extract_divisions(request)
    show_in_space = json.loads(request.GET.get("space", "true"))
    show_in_stations = json.loads(request.GET.get("stations", "true"))
    
    where = []
    if not show_in_space:
        where.append('"stationID" < %d' % constants.NPC_LOCATION_IDS)
    if not show_in_stations:
        where.append('"stationID" > %d' % constants.NPC_LOCATION_IDS)
    if divisions is not None:
        where.append('"hangarID" IN %s')
    
    sql = 'SELECT "solarSystemID", COUNT(*) AS "items" FROM "assets_assetdiff" '
    sql += 'WHERE date=%s'
    if where: sql += ' AND ' + ' AND '.join(where)
    sql += ' GROUP BY "solarSystemID";'

    cursor = connection.cursor()
    if divisions is None:
        cursor.execute(sql, [date])
    else:
        cursor.execute(sql, [date, divisions])
    
    jstree_data = []
    for solarSystemID, items in cursor:
        name, security = db.resolveLocationName(solarSystemID)
        if security > 0.5:
            color = "hisec"
        elif security > 0:
            color = "lowsec"
        else:
            color = "nullsec"
        jstree_data.append({
            "data" : HTML_ITEM_SPAN % (name, items, pluralize(items)),
            "attr" : { 
                "id" : "_%d" % solarSystemID, 
                "rel" : "system",
                "sort_key" : name.lower(),
                "class" : "system-%s-row" % color 
            },
            "state" : "closed"
        })
    cursor.close()
    return HttpResponse(json.dumps(jstree_data))

#------------------------------------------------------------------------------
@check_user_access()
@cache_page(3 * 60 * 60) # 3 hours cache
def stations_data(request, date_str, solarSystemID):
    date = datetime.strptime(date_str, DATE_PATTERN)
    solarSystemID = int(solarSystemID)
    divisions = extract_divisions(request)
    show_in_space = json.loads(request.GET.get("space", "true"))
    show_in_stations = json.loads(request.GET.get("stations", "true"))
    
    where = []
    if not show_in_space:
        where.append('"stationID" < %d' % constants.NPC_LOCATION_IDS)
    if not show_in_stations:
        where.append('"stationID" > %d' % constants.NPC_LOCATION_IDS)
    if divisions is not None:
        where.append('"hangarID" IN %s')
    
    sql = 'SELECT "stationID", MAX("flag") as "flag", COUNT(*) AS "items" FROM "assets_assetdiff" '
    sql += 'WHERE "solarSystemID"=%s AND "date"=%s '
    if where: sql += ' AND ' + ' AND '.join(where)
    sql += ' GROUP BY "stationID";'
     
    cursor = connection.cursor()
    if divisions is None:
        cursor.execute(sql, [solarSystemID, date])
    else:
        cursor.execute(sql, [solarSystemID, date, divisions])
        
    jstree_data = []
    for stationID, flag, items in cursor:
        if stationID < constants.NPC_LOCATION_IDS:
            # it's a real station
            name = db.resolveLocationName(stationID)[0]
            icon = "station"
        else:
            # it is an inspace anchorable array
            name = db.resolveTypeName(flag)[0]
            icon = "array"
        
        jstree_data.append({
            "data" : HTML_ITEM_SPAN % (name, items, pluralize(items)),
            "attr" : { 
                "id" : "_%d_%d" % (solarSystemID, stationID), 
                "sort_key" : stationID,
                "rel" : icon,
                "class" : "%s-row" % icon
            },
            "state" : "closed"
        })
    cursor.close()
    return HttpResponse(json.dumps(jstree_data))


#------------------------------------------------------------------------------
@check_user_access()
@cache_page(3 * 60 * 60) # 3 hours cache
def hangars_data(request, date_str, solarSystemID, stationID):
    
    date = datetime.strptime(date_str, DATE_PATTERN)
    solarSystemID = int(solarSystemID)
    stationID = int(stationID)
    divisions = extract_divisions(request)
    
    where = []
    if divisions is not None:
        where.append('"hangarID" IN %s')
    
    sql = 'SELECT "hangarID", COUNT(*) AS "items" FROM "assets_assetdiff" '
    sql += 'WHERE "solarSystemID"=%s AND "stationID"=%s AND "date"=%s '
    if where: sql += ' AND ' + ' AND '.join(where)
    sql += ' GROUP BY "hangarID";'
    
    cursor = connection.cursor()
    if divisions is None:
        cursor.execute(sql, [solarSystemID, stationID, date])
    else:
        cursor.execute(sql, [solarSystemID, stationID, date, divisions])
    
    HANGAR = {}
    for h in Hangar.objects.all():
        HANGAR[h.hangarID] = h.name
    
    jstree_data = []
    for hangarID, items in cursor.fetchall():
        jstree_data.append({
            "data": HTML_ITEM_SPAN % (HANGAR[hangarID], items, pluralize(items)),
            "attr" : { 
                "id" : "_%d_%d_%d" % (solarSystemID, stationID, hangarID),
                "sort_key" : hangarID,
                "rel" : "hangar",
                "class" : "hangar-row"
            },
            "state" : "closed"
        })
    
    return HttpResponse(json.dumps(jstree_data))

#------------------------------------------------------------------------------
@check_user_access()
@cache_page(3 * 60 * 60) # 3 hours cache
def hangar_contents_data(request, date_str, solarSystemID, stationID, hangarID):
    date = datetime.strptime(date_str, DATE_PATTERN)
    solarSystemID = int(solarSystemID)
    stationID = int(stationID)
    hangarID = int(hangarID)
    
    query = AssetDiff.objects.filter(solarSystemID=solarSystemID,
                                     stationID=stationID, hangarID=hangarID,
                                     date=date)
    jstree_data = []
    for item in query:
        name = db.resolveTypeName(item.typeID)[0]
        
        if item.quantity < 0:
            icon = "removed"
        else:
            icon = "added"
        
        jstree_data.append({
            "data": "%s <i>(%s)</i>" % (name, utils.print_quantity(item.quantity)),
            "attr" : { 
                "sort_key" : name.lower(),
                "rel" : icon,
                "class" : "%s-row" % icon
            }
        })

    return HttpResponse(json.dumps(jstree_data))

#------------------------------------------------------------------------------
@check_user_access()
@cache_page(3 * 60 * 60) # 3 hours cache
def search_items(request, date_str):
    date = datetime.strptime(date_str, DATE_PATTERN)
    divisions = extract_divisions(request)
    show_in_space = json.loads(request.GET.get("space", "true"))
    show_in_stations = json.loads(request.GET.get("stations", "true"))
    search_string = request.GET.get("search_string", "no-item")
    
    matchingIDs = db.getMatchingIdsFromString(search_string)
    
    query = AssetDiff.objects.filter(typeID__in=matchingIDs, date=date)
    
    if divisions is not None:
        query = query.filter(hangarID__in=divisions)
    if not show_in_space:
        query = query.filter(stationID__lt=constants.NPC_LOCATION_IDS)
    if not show_in_stations:
        query = query.filter(stationID__gt=constants.NPC_LOCATION_IDS)


    json_data = []

    for item in query:
        nodeid = "#_%d" % item.solarSystemID
        json_data.append(nodeid)
        nodeid = nodeid + "_%d" % item.stationID
        json_data.append(nodeid)
        nodeid = nodeid + "_%d" % item.hangarID
        json_data.append(nodeid)
    
    return HttpResponse(json.dumps(json_data))
