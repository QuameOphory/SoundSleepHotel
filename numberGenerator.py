def generateRoomNumber(qs, prefix='DEF', postfix='1', length=6):
    if qs.count() == 0:
        return prefix + postfix.zfill(length - 3)
    else:
        firstrecord = qs.first()
        postfix = str(int(firstrecord.room_number[3:]) + 1)
        return prefix + postfix.zfill(length - len(postfix))