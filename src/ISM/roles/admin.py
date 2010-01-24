'''
This file is part of ICE Security Management

Created on 24 janv. 2010

@author: diabeteman
'''

from ISM.roles.models import Role, Character, Title, RoleType, RoleMembership, TitleMembership, TitleComposition
from django.contrib import admin

admin.site.register(Role)
admin.site.register(Title)
admin.site.register(Character)
admin.site.register(RoleType)
admin.site.register(RoleMembership)
admin.site.register(TitleMembership)
admin.site.register(TitleComposition)
