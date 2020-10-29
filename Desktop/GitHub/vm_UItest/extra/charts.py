#   d1    =   7d6b7226-24f3-47f7-9bcb-a6f13223915d
#   d2    =   f17b542b-4ffe-4f71-b91e-2d9701d17099
#   d3    =   499a8179-a4d3-4158-be02-d005f01bf6cd

#   2020/10/02 10:00:00 = 1601604000000


#写文档、测Email、Platform需求



#访客-越权
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601604000000
            deviceUuid:"7d6b7226-24f3-47f7-9bcb-a6f13223915d"
            accessType:ILLEGAL
            identityType:TEMP_VISITOR
            visitor:{id:"413"}
        }
    )
}
"""


#访客-正常
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601604000000
            deviceUuid:"7d6b7226-24f3-47f7-9bcb-a6f13223915d"
            accessType:NORMAL
            identityType:TEMP_VISITOR
            visitor:{id:"413"}
        }
    )
}
"""


#黑名单
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601604000000
            deviceUuid:"499a8179-a4d3-4158-be02-d005f01bf6cd"
            accessType:BLACKLIST
            identityType:BLACKLIST
            member:{id:"200"}
        }
    )
}
"""


#陌生人-未识别
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601604000000
            deviceUuid:"499a8179-a4d3-4158-be02-d005f01bf6cd"
            accessType:FORBIDDEN
            identityType:STRANGER
        }
    )
}
"""




#1601611200000 ///////12点

#陌生人-多组匹配
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601611200000
            deviceUuid:"499a8179-a4d3-4158-be02-d005f01bf6cd"
            accessType:MULTI_MATCH
            identityType:STRANGER
        }
    )
}
"""



#1601697600000 /////3号


#员工-越权
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601697600000
            deviceUuid:"f17b542b-4ffe-4f71-b91e-2d9701d17099"
            accessType:ILLEGAL
            identityType:ID
            member:{id:"181"}
        }
    )
}
"""


#员工-正常
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601697600000
            deviceUuid:"7d6b7226-24f3-47f7-9bcb-a6f13223915d"
            accessType:NORMAL
            identityType:ID
            member:{id:"180"}
        }
    )
}
"""


#其他人员-越权
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601697600000
            deviceUuid:"7d6b7226-24f3-47f7-9bcb-a6f13223915d"
            accessType:ILLEGAL
            identityType:OTHER
            member:{id:"198"}
        }
    )
}
"""


#其他人员-正常
body = """
mutation{
    createMemberRecord(
        memberRecord:{
            start:1601697600000
            deviceUuid:"7d6b7226-24f3-47f7-9bcb-a6f13223915d"
            accessType:NORMAL
            identityType:OTHER
            member:{id:"199"}
        }
    )
}
"""


