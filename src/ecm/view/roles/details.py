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

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.cache import cache_page
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils.text import truncate_words

from ecm.data.roles.models import Role, RoleType, Member
from ecm.data.common.models import ColorThreshold
from ecm.core.auth import user_is_director
from ecm.core.utils import print_date
from ecm.view.members import member_table_columns

#------------------------------------------------------------------------------
@cache_page(3 * 60 * 60) # 3 hours cache
@user_is_director()
def role(request, role_typeName, role_id):
    try:
        type = RoleType.objects.get(typeName=role_typeName)
        role = Role.objects.get(roleType=type, roleID=int(role_id))
        role.accessLvl = role.get_access_lvl()
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    
    thresholds = list(ColorThreshold.objects.all().order_by("threshold").values("threshold", "color"))
    data = {
        'colorThresholds' : json.dumps(thresholds),
        'role_types' : RoleType.objects.all(),
        'role' : role,
        'direct_member_count' : role.members.count(),
        'total_member_count' : role.members_through_titles().count()
    }
    return render_to_response("roles/role_details.html", data, context_instance=RequestContext(request))



#------------------------------------------------------------------------------
@cache_page(3 * 60 * 60) # 3 hours cache
@user_is_director()
def role_data(request, role_typeName, role_id):
    try:
        iDisplayStart = int(request.GET["iDisplayStart"])
        iDisplayLength = int(request.GET["iDisplayLength"])
        sSearch = request.GET["sSearch"]
        sEcho = int(request.GET["sEcho"])
        type = RoleType.objects.get(typeName=role_typeName)
        role = Role.objects.get(roleType=type, roleID=int(role_id))
        
        try:
            column = int(request.GET["iSortCol_0"])
            ascending = (request.GET["sSortDir_0"] == "asc")
        except:
            column = 0
            ascending = True
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseBadRequest()

    total_members,\
    filtered_members,\
    members = getMembers(role=role,
                         first_id=iDisplayStart, 
                         last_id=iDisplayStart + iDisplayLength - 1,
                         search_str=sSearch,
                         sort_by=member_table_columns[column], 
                         asc=ascending)
    json_data = {
        "sEcho" : sEcho,
        "iTotalRecords" : total_members,
        "iTotalDisplayRecords" : filtered_members,
        "aaData" : members
    }
    
    return HttpResponse(json.dumps(json_data))


#------------------------------------------------------------------------------
def getMembers(role, first_id, last_id, search_str=None, sort_by="name", asc=True):

    sort_col = "%s_nocase" % sort_by
    
    members = role.members_through_titles(with_direct_roles=True)

    # SQLite hack for making a case insensitive sort
    members = members.extra(select={sort_col : "%s COLLATE NOCASE" % sort_by})
    if not asc: sort_col = "-" + sort_col
    members = members.extra(order_by=[sort_col])
    
    if search_str:
        total_members = members.count()
        search_args = Q(name__icontains=search_str) | Q(nickname__icontains=search_str)
        
        if "DIRECTOR".startswith(search_str.upper()):
            search_args = search_args | Q(accessLvl=Member.DIRECTOR_ACCESS_LVL)
        
        members = members.filter(search_args)
        filtered_members = members.count()
    else:
        total_members = filtered_members = members.count()
    
    members = members[first_id:last_id]
    
    member_list = []
    for m in members:
        titles = ["Titles"]
        titles.extend([ str(t) for t in m.titles.all() ])
        memb = [
            m.as_html(),
            truncate_words(m.nickname, 5),
            m.accessLvl,
            print_date(m.corpDate),
            print_date(m.lastLogin),
            truncate_words(m.location, 5),
            "|".join(titles),
        ] 

        member_list.append(memb)
    
    return total_members, filtered_members, member_list