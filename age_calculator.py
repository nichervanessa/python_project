#Age Calculator
def age_real(y,m,d):
    import datetime
    x=int(input("Pleas Enter Your Year:"))
    y=int(input("pleaser Enter Month No:"))
    z=int(input("Please enter days:"))
    today=datetime.datetime.now().date()
    date_of_birth=datetime.date(y,m,d)
    age=int((today-date_of_birth).days /365.5)
    print(age)

age_real(1992,11,1)
