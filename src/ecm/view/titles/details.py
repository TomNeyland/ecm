# The MIT License - EVE Corporation Management
# 
# Copyright (c) 2010 Robin Jarry
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__date__ = "2011-03-13"
__author__ = "diabeteman"

import json

from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from ecm.data.roles.models import TitleComposition, TitleCompoDiff, Title
from ecm.core import utils
from ecm.data.common.models import ColorThreshold
from ecm.core.utils import get_access_color
from ecm.core.auth import user_is_director


#------------------------------------------------------------------------------
@cache_page(3 * 60 * 60) # 3 hours cache
@user_is_director()
def details(request, id):
    colorThresholds = []
    for c in ColorThreshold.objects.all().order_by("threshold"):
        colorThresholds.append({ "threshold" : c.threshold, "color" : c.color })
    
    title = Title.objects.get(titleID=int(id))
    title.lastModified = TitleCompoDiff.objects.filter(title=title).order_by("-id")
    if title.lastModified.count():
        title.lastModified = utils.print_time_min(title.lastModified[0].date)
    else:
        title.lastModified = None
    title.color = get_access_color(title.accessLvl, ColorThreshold.objects.all().order_by("threshold"))

    data = { "title" : title,
            "member_count" : title.members.count(),  
            "colorThresholds" : json.dumps(colorThresholds) }

    return render_to_response("titles/title_details.html", data, RequestContext(request))




#------------------------------------------------------------------------------
composition_columns = [ "role_id" ]
@cache_page(3 * 60 * 60) # 3 hours cache
@user_is_director()
def composition_data(request, id):
    iDisplayStart = int(request.GET["iDisplayStart"])
    iDisplayLength = int(request.GET["iDisplayLength"])
    sEcho = int(request.GET["sEcho"])
    column = int(request.GET["iSortCol_0"])
    ascending = (request.GET["sSortDir_0"] == "asc")

    total_compos, composition = getTitleComposition(id=int(id),
                                                    first_id=iDisplayStart,
                                                    last_id=iDisplayStart + iDisplayLength - 1,
                                                    sort_by=composition_columns[column], 
                                                    asc=ascending)
    json_data = {
        "sEcho" : sEcho,
        "iTotalRecords" : total_compos,
        "iTotalDisplayRecords" : total_compos,
        "aaData" : composition
    }
    
    return HttpResponse(json.dumps(json_data))







#------------------------------------------------------------------------------
def getTitleComposition(id, first_id, last_id, sort_by="role_id", asc=True):

    sort_col = "%s_nocase" % sort_by
    
    compos = TitleComposition.objects.filter(title=id)

    # SQLite hack for making a case insensitive sort
    compos = compos.extra(select={sort_col : "%s COLLATE NOCASE" % sort_by})
    if not asc: sort_col = "-" + sort_col
    compos = compos.extra(order_by=[sort_col])
    
    total_compos = compos.count()
    
    compos = compos[first_id:last_id]
    
    compo_list = []
    for c in compos:
        compo_list.append([
            c.role.as_html(),
            c.role.get_access_lvl()
        ])
    
    return total_compos, compo_list



#------------------------------------------------------------------------------
@cache_page(3 * 60 * 60) # 3 hours cache
@user_is_director()
def compo_diff_data(request, id):
    iDisplayStart = int(request.GET["iDisplayStart"])
    iDisplayLength = int(request.GET["iDisplayLength"])
    sEcho = int(request.GET["sEcho"])

    total_diffs, diffs = getTitleCompoDiff(id=int(id),
                                           first_id=iDisplayStart,
                                           last_id=iDisplayStart + iDisplayLength - 1)
    json_data = {
        "sEcho" : sEcho,
        "iTotalRecords" : total_diffs,
        "iTotalDisplayRecords" : total_diffs,
        "aaData" : diffs
    }
    
    return HttpResponse(json.dumps(json_data))


#------------------------------------------------------------------------------
def getTitleCompoDiff(id, first_id, last_id):

    diffsDb = TitleCompoDiff.objects.filter(title=id).order_by("-date")
    total_diffs = diffsDb.count()
    
    diffsDb = diffsDb[first_id:last_id]
    
    diff_list = []
    for d in diffsDb:
        diff = [
            d.new,
            '<a href="/roles/%s/%d" class="role">%s</a>' % (d.role.roleType.typeName, d.role.roleID, unicode(d.role)),
            utils.print_time_min(d.date)
        ] 

        diff_list.append(diff)
    
    return total_diffs, diff_list
