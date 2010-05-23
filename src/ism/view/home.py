'''
This file is part of ICE Security Management

Created on 3 fev. 2010
@author: diabeteman
'''

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

from ism.data.roles.models import MemberDiff, RoleMemberDiff, TitleCompoDiff, Member
from ism.core.utils import print_time_min

#------------------------------------------------------------------------------
@login_required
def home(request):
    data = {               'members' : getLastMembers(),
                    'last_role_adds' : getLastRoleAdds(),
                'last_role_removals' : getLastRoleRemovals(),
              'last_title_role_adds' : getLastTitleRoleAdds(),
          'last_title_role_removals' : getLastTitleRoleRemovals()  }
    
    return render_to_response("home.html", data, context_instance=RequestContext(request))

#------------------------------------------------------------------------------
def getLastMembers(count=5):
    members = getLastCorpedMembers(count)
    members.extend(getLastExpelledMembers(count))
    members.sort(key=lambda m: m.date, reverse=True)
    return members

#------------------------------------------------------------------------------
def getLastCorpedMembers(count=5):
    queryset = list(MemberDiff.objects.filter(new=True).order_by('-id'))[:count]
    members = []
    for m in queryset:
        if m.new:
            memb = Member.objects.get(characterID=m.characterID)
            m.nickname = memb.nickname
            m.date = print_time_min(memb.corpDate)
        else:
            m.date = print_time_min(m.date)
        members.append(m)
    return members

#------------------------------------------------------------------------------
def getLastExpelledMembers(count=5):
    queryset = list(MemberDiff.objects.filter(new=False).order_by('-id'))[:count]
    members = []
    for m in queryset:
        if m.new:
            memb = Member.objects.get(characterID=m.characterID)
            m.nickname = memb.nickname
            m.date = print_time_min(memb.corpDate)
        else:
            m.date = print_time_min(m.date)
        members.append(m)
    return members

#------------------------------------------------------------------------------
def getLastRoleAdds(count=10):
    roles = RoleMemberDiff.objects.filter(new=True).order_by('-id')[:count]
    for r in roles:
        r.date = print_time_min(r.date)
    return roles

#------------------------------------------------------------------------------
def getLastRoleRemovals(count=10):
    roles = RoleMemberDiff.objects.filter(new=False).order_by('-id')[:count]
    for r in roles:
        r.date = print_time_min(r.date)
    return roles

#------------------------------------------------------------------------------
def getLastTitleRoleAdds(count=10):
    titles = TitleCompoDiff.objects.filter(new=True).order_by('-id')[:count]
    for t in titles:
        t.date = print_time_min(t.date)
    return titles

#------------------------------------------------------------------------------
def getLastTitleRoleRemovals(count=10):
    titles = TitleCompoDiff.objects.filter(new=False).order_by('-id')[:count]
    for t in titles:
        t.date = print_time_min(t.date)
    return titles
#------------------------------------------------------------------------------