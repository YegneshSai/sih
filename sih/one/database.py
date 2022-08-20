import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="sih"
)
mycursor=mydb.cursor()
def add_user(v):
    try:
        add_record="insert into user values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(add_record,v)
        mydb.commit()
        return True
    except:
        print("errorrrrrrrrrrr")
        return False

def add_mechanic(v):

    add_record="insert into mechanic values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(add_record,v)
    mydb.commit()
    return True
    # except:
    #     print("errorrrrrrrrrrr")
    #     return False


def check_user(user_id,passwod):
    check_record = "select password from user where phno=%s"
    user_id=[user_id]
    mycursor.execute(check_record, user_id)
    print()
    l=mycursor.fetchall()[0][0]
    print(l)

    if passwod ==l:
        return True
    else:
        return False


def check_mechanic(user_id,passwod):
    check_record = "select password from mechanic where phno=%s"
    user_id=[user_id]
    mycursor.execute(check_record, user_id)
    print()
    l=mycursor.fetchall()[0][0]
    print(l)

    if passwod ==l:
        return True
    else:
        return False

def get_mechanic(user,location):
    q="select * from mechanic where location=%s"
    v=[location]
    mycursor.execute(q,v)
    l = []
    for i in mycursor:
        l.append(list(i))
    return l