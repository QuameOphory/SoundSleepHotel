from datetime import date


def generateRoomNumber(qs, prefix='DEF', postfix='1', length=6):
    if qs.count() == 0:
        return prefix + postfix.zfill(length - 3)
    else:
        firstrecord = qs.first()
        postfix = str(int(firstrecord.room_number[3:]) + 1)
        return prefix + postfix.zfill(length - 3)

def generateClientNumber(prefix, qs, postfix='1'):
    today = date.today()
    today_str = str(today).split('-')
    year = today_str[0]
    today_str[0] = year[2:]
    datepart = ''.join(today_str)
    if qs.count()==0:
        numberstring = prefix + datepart + postfix.zfill(6)
        return numberstring
    else:
        firstrecord = qs.first()
        clientnumber, new_clientnumber = firstrecord.client_number[7:], str(int(firstrecord.client_number[7:]) + 1)
        # lenofnewnumber = len(new_clientnumber)
        # diff = len(clientnumber) - lenofnewnumber
        # postfix = new_clientnumber.zfill(lenofnewnumber + diff)
        postfix = new_clientnumber.zfill(len(clientnumber))
        numberstring = prefix + datepart + postfix
        return numberstring


def generateBookingNumber(qs, prefix='B', postfix='1'):
    today = date.today()
    today_str = str(today).split('-')
    year = today_str[0]
    today_str[0] = year[2:]
    datepart = ''.join(today_str)
    if qs.count()==0:
        numberstring = prefix + datepart + postfix.zfill(6)
        return numberstring
    else:
        firstrecord = qs.first()
        bookingnumber, new_bookingnumber = firstrecord.booking_number[7:], str(int(firstrecord.booking_number[7:]) + 1)
        postfix = new_bookingnumber.zfill(len(bookingnumber))
        numberstring = prefix + datepart + postfix
        return numberstring