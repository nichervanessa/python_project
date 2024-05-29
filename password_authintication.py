#Password Authitication 

import getpass
#dictionary
memory={"Nichervan.Essa":12345,"Shirwan.Essa":54321,"Safwan.Essa":123456,"Yaseen.Hassan":654321}
username=input("Enter Your username Please:")
#that we add from our moduls
password=getpass.getpass("Enter Your Password:")
#for loops
for i in memory.keys():

    if username ==i:
        while password !=memory.get(i):
            password=getpass.getpass("Enter Your Password again:")
            break
        print("Verified")
    elif password !=i:
        print("Your password is not correct please enter again:")
    else:
        print("Your Username is not available")
