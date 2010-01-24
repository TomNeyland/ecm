﻿'''
This file is part of ICE Security Management

Created on 24 janv. 2010

@author: diabeteman
'''

from ISM.roles.models import RoleType, Role


def init():
    #---------------------#
    # ROLE TYPES CREATION #
    #---------------------#
    print "Creating role categories..."
    RoleType(typeName='roles').save()
    RoleType(typeName='grantableRoles').save()
    RoleType(typeName='rolesAtHQ').save()
    RoleType(typeName='grantableRolesAtHQ').save()
    RoleType(typeName='rolesAtBase').save()
    RoleType(typeName='grantableRolesAtBase').save()
    RoleType(typeName='rolesAtOther').save()
    RoleType(typeName='grantableRolesAtOther').save()

    #----------------#
    # ROLES CREATION #
    #----------------#
    # roles
    print "Creating roles..."
    Role(roleID=1, roleName="roleDirector", description="Can do anything the CEO can do. Including giving roles to anyone.", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=128, roleName="rolePersonnelManager", description="Can accept applications to join the corporation.", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=256, roleName="roleAccountant", description="Can view/use corporation accountancy info.", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=512, roleName="roleSecurityOfficer", description="Can view the content of others hangars", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=1024, roleName="roleFactoryManager", description="Can perform factory management tasks.", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=2048, roleName="roleStationManager", description="Can perform station management for a corporation.", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=4096, roleName="roleAuditor", description="Can perform audits on corporation security event logs", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=134217728, roleName="roleAccountCanTake1", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=268435456, roleName="roleAccountCanTake2", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=536870912, roleName="roleAccountCanTake3", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=1073741824, roleName="roleAccountCanTake4", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=2147483648, roleName="roleAccountCanTake5", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=4294967296, roleName="roleAccountCanTake6", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=8589934592, roleName="roleAccountCanTake7", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=2199023255552, roleName="roleEquipmentConfig", description="Can deploy and configure equipment in space.", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=562949953421312, roleName="roleCanRentOffice", description="When assigned to a member, the member can rent offices on behalf of the corporation", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=1125899906842624, roleName="roleCanRentFactorySlot", description="When assigned to a member, the member can rent factory slots on behalf of the corporation", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=2251799813685248, roleName="roleCanRentResearchSlot", description="When assigned to a member, the member can rent research facilities on behalf of the corporation", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=4503599627370496, roleName="roleJuniorAccountant", description="Can view corporation accountancy info.", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=9007199254740992, roleName="roleStarbaseConfig", description="Can deploy and configure starbase structures in space.", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=18014398509481984, roleName="roleTrader", description="Can buy and sell things for the corporation", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=36028797018963968, roleName="roleChatManager", description="Can moderate corporation/alliance communications channels", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=72057594037927936, roleName="roleContractManager", description="Can create, edit and oversee all contracts made on behalf of the corportation as well as accept contracts on behalf of the corporation", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=144115188075855872, roleName="roleInfrastructureTacticalOfficer", description="Can operate defensive starbase structures", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=288230376151711744, roleName="roleStarbaseCaretaker", description="Can refuel starbases and take from silo bins", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    Role(roleID=576460752303423488, roleName="roleFittingManager", description="Can add and delete fittings", roleType_id=RoleType.objects.filter(typeName='roles')[0].id).save()
    
    # grantableRoles
    print "Creating grantableRoles..."
    Role(roleID=128, roleName="rolePersonnelManager", description="Can accept applications to join the corporation.", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=256, roleName="roleAccountant", description="Can view/use corporation accountancy info.", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=512, roleName="roleSecurityOfficer", description="Can view the content of others hangars", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=1024, roleName="roleFactoryManager", description="Can perform factory management tasks.", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=2048, roleName="roleStationManager", description="Can perform station management for a corporation.", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=4096, roleName="roleAuditor", description="Can perform audits on corporation security event logs", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=134217728, roleName="roleAccountCanTake1", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=268435456, roleName="roleAccountCanTake2", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=536870912, roleName="roleAccountCanTake3", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=1073741824, roleName="roleAccountCanTake4", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=2147483648, roleName="roleAccountCanTake5", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=4294967296, roleName="roleAccountCanTake6", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=8589934592, roleName="roleAccountCanTake7", description="Can take funds from this divisions account", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=2199023255552, roleName="roleEquipmentConfig", description="Can deploy and configure equipment in space.", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=562949953421312, roleName="roleCanRentOffice", description="When assigned to a member, the member can rent offices on behalf of the corporation", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=1125899906842624, roleName="roleCanRentFactorySlot", description="When assigned to a member, the member can rent factory slots on behalf of the corporation", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=2251799813685248, roleName="roleCanRentResearchSlot", description="When assigned to a member, the member can rent research facilities on behalf of the corporation", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=4503599627370496, roleName="roleJuniorAccountant", description="Can view corporation accountancy info.", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=9007199254740992, roleName="roleStarbaseConfig", description="Can deploy and configure starbase structures in space.", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=18014398509481984, roleName="roleTrader", description="Can buy and sell things for the corporation", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=36028797018963968, roleName="roleChatManager", description="Can moderate corporation/alliance communications channels", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=72057594037927936, roleName="roleContractManager", description="Can create, edit and oversee all contracts made on behalf of the corportation as well as accept contracts on behalf of the corporation", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=144115188075855872, roleName="roleInfrastructureTacticalOfficer", description="Can operate defensive starbase structures", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=288230376151711744, roleName="roleStarbaseCaretaker", description="Can refuel starbases and take from silo bins", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    Role(roleID=576460752303423488, roleName="roleFittingManager", description="Can add and delete fittings", roleType_id=RoleType.objects.filter(typeName='grantableRoles')[0].id).save()
    
    # rolesAtHQ
    print "Creating rolesAtHQ..."
    Role(roleID=1, roleName="roleDirector", description="Can do anything the CEO can do. Including giving roles to anyone.", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=8192, roleName="roleHangarCanTake1", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=16384, roleName="roleHangarCanTake2", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=32768, roleName="roleHangarCanTake3", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=65536, roleName="roleHangarCanTake4", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=131072, roleName="roleHangarCanTake5", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=262144, roleName="roleHangarCanTake6", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=524288, roleName="roleHangarCanTake7", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=1048576, roleName="roleHangarCanQuery1", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=2097152, roleName="roleHangarCanQuery2", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=4194304, roleName="roleHangarCanQuery3", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=8388608, roleName="roleHangarCanQuery4", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=16777216, roleName="roleHangarCanQuery5", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=33554432, roleName="roleHangarCanQuery6", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=67108864, roleName="roleHangarCanQuery7", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=4398046511104, roleName="roleContainerCanTake1", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=8796093022208, roleName="roleContainerCanTake2", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=17592186044416, roleName="roleContainerCanTake3", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=35184372088832, roleName="roleContainerCanTake4", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=70368744177664, roleName="roleContainerCanTake5", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=140737488355328, roleName="roleContainerCanTake6", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    Role(roleID=281474976710656, roleName="roleContainerCanTake7", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtHQ')[0].id).save()
    
    # grantableRolesAtHQ
    print "Creating grantableRolesAtHQ..."
    Role(roleID=8192, roleName="roleHangarCanTake1", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=16384, roleName="roleHangarCanTake2", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=32768, roleName="roleHangarCanTake3", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=65536, roleName="roleHangarCanTake4", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=131072, roleName="roleHangarCanTake5", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=262144, roleName="roleHangarCanTake6", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=524288, roleName="roleHangarCanTake7", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=1048576, roleName="roleHangarCanQuery1", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=2097152, roleName="roleHangarCanQuery2", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=4194304, roleName="roleHangarCanQuery3", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=8388608, roleName="roleHangarCanQuery4", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=16777216, roleName="roleHangarCanQuery5", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=33554432, roleName="roleHangarCanQuery6", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=67108864, roleName="roleHangarCanQuery7", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=4398046511104, roleName="roleContainerCanTake1", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=8796093022208, roleName="roleContainerCanTake2", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=17592186044416, roleName="roleContainerCanTake3", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=35184372088832, roleName="roleContainerCanTake4", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=70368744177664, roleName="roleContainerCanTake5", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=140737488355328, roleName="roleContainerCanTake6", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    Role(roleID=281474976710656, roleName="roleContainerCanTake7", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtHQ')[0].id).save()
    
    # rolesAtBase
    print "Creating rolesAtBase..."
    Role(roleID=1, roleName="roleDirector", description="Can do anything the CEO can do. Including giving roles to anyone.", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=8192, roleName="roleHangarCanTake1", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=16384, roleName="roleHangarCanTake2", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=32768, roleName="roleHangarCanTake3", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=65536, roleName="roleHangarCanTake4", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=131072, roleName="roleHangarCanTake5", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=262144, roleName="roleHangarCanTake6", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=524288, roleName="roleHangarCanTake7", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=1048576, roleName="roleHangarCanQuery1", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=2097152, roleName="roleHangarCanQuery2", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=4194304, roleName="roleHangarCanQuery3", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=8388608, roleName="roleHangarCanQuery4", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=16777216, roleName="roleHangarCanQuery5", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=33554432, roleName="roleHangarCanQuery6", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=67108864, roleName="roleHangarCanQuery7", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=4398046511104, roleName="roleContainerCanTake1", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=8796093022208, roleName="roleContainerCanTake2", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=17592186044416, roleName="roleContainerCanTake3", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=35184372088832, roleName="roleContainerCanTake4", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=70368744177664, roleName="roleContainerCanTake5", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=140737488355328, roleName="roleContainerCanTake6", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    Role(roleID=281474976710656, roleName="roleContainerCanTake7", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtBase')[0].id).save()
    
    # grantableRolesAtBase
    print "Creating grantableRolesAtBase..."
    Role(roleID=8192, roleName="roleHangarCanTake1", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=16384, roleName="roleHangarCanTake2", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=32768, roleName="roleHangarCanTake3", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=65536, roleName="roleHangarCanTake4", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=131072, roleName="roleHangarCanTake5", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=262144, roleName="roleHangarCanTake6", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=524288, roleName="roleHangarCanTake7", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=1048576, roleName="roleHangarCanQuery1", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=2097152, roleName="roleHangarCanQuery2", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=4194304, roleName="roleHangarCanQuery3", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=8388608, roleName="roleHangarCanQuery4", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=16777216, roleName="roleHangarCanQuery5", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=33554432, roleName="roleHangarCanQuery6", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=67108864, roleName="roleHangarCanQuery7", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=4398046511104, roleName="roleContainerCanTake1", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=8796093022208, roleName="roleContainerCanTake2", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=17592186044416, roleName="roleContainerCanTake3", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=35184372088832, roleName="roleContainerCanTake4", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=70368744177664, roleName="roleContainerCanTake5", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=140737488355328, roleName="roleContainerCanTake6", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    Role(roleID=281474976710656, roleName="roleContainerCanTake7", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtBase')[0].id).save()
    
    # rolesAtOther
    print "Creating rolesAtOther..."
    Role(roleID=1, roleName="roleDirector", description="Can do anything the CEO can do. Including giving roles to anyone.", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=8192, roleName="roleHangarCanTake1", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=16384, roleName="roleHangarCanTake2", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=32768, roleName="roleHangarCanTake3", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=65536, roleName="roleHangarCanTake4", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=131072, roleName="roleHangarCanTake5", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=262144, roleName="roleHangarCanTake6", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=524288, roleName="roleHangarCanTake7", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=1048576, roleName="roleHangarCanQuery1", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=2097152, roleName="roleHangarCanQuery2", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=4194304, roleName="roleHangarCanQuery3", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=8388608, roleName="roleHangarCanQuery4", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=16777216, roleName="roleHangarCanQuery5", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=33554432, roleName="roleHangarCanQuery6", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=67108864, roleName="roleHangarCanQuery7", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=4398046511104, roleName="roleContainerCanTake1", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=8796093022208, roleName="roleContainerCanTake2", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=17592186044416, roleName="roleContainerCanTake3", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=35184372088832, roleName="roleContainerCanTake4", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=70368744177664, roleName="roleContainerCanTake5", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=140737488355328, roleName="roleContainerCanTake6", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    Role(roleID=281474976710656, roleName="roleContainerCanTake7", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='rolesAtOther')[0].id).save()
    
    # grantableRolesAtOther
    print "Creating grantableRolesAtOther..."
    Role(roleID=8192, roleName="roleHangarCanTake1", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=16384, roleName="roleHangarCanTake2", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=32768, roleName="roleHangarCanTake3", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=65536, roleName="roleHangarCanTake4", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=131072, roleName="roleHangarCanTake5", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=262144, roleName="roleHangarCanTake6", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=524288, roleName="roleHangarCanTake7", description="Can take items from this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=1048576, roleName="roleHangarCanQuery1", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=2097152, roleName="roleHangarCanQuery2", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=4194304, roleName="roleHangarCanQuery3", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=8388608, roleName="roleHangarCanQuery4", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=16777216, roleName="roleHangarCanQuery5", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=33554432, roleName="roleHangarCanQuery6", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=67108864, roleName="roleHangarCanQuery7", description="Can query the content of this divisions hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=4398046511104, roleName="roleContainerCanTake1", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=8796093022208, roleName="roleContainerCanTake2", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=17592186044416, roleName="roleContainerCanTake3", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=35184372088832, roleName="roleContainerCanTake4", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=70368744177664, roleName="roleContainerCanTake5", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=140737488355328, roleName="roleContainerCanTake6", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    Role(roleID=281474976710656, roleName="roleContainerCanTake7", description="Can take containers from this divisional hangar", roleType_id=RoleType.objects.filter(typeName='grantableRolesAtOther')[0].id).save()
    print ""