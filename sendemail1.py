def sendemail():
    yn = input("Enter your name:")
    regno = input("Enter Reg No.")
    name = input("Enter recepient name:")
    tim = input("Enter time slot: FN/AN")
    sub = input("Enter subject:")
    lst1 = ['juliet@vjcet.org','anitta@vjcet.org']
    eid = "juliet@vjcet.org"
    if name == "juliet":
        eid = lst1[0]
    elif name == "anitta":
        eid = lst1[1]

    textdata = yn +"(" +regno + ")" + "has requested for an appointment at "+ tim + " session. Request has been sent to "+ eid + "." 
    print(textdata)

sendemail()