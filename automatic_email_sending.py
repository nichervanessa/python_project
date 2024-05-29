#Sending Automatic Email using Google Account
#anoj mvyn nvdx nepo


import os
import random
import smtplib

def automatic_email():
    user=input("Enter Your Username >>:")
    emails=input("Please Enter Your email>>>:")
    message=(f"Dear Hello {user} ,welcome to block tech academy")

    d=smtplib.SMTP("smtp.gmail.com",587)
    d.starttls()
    d.login("nichervan.essa92@gmail.com","anoj mvyn nvdx nepo")
    d.sendmail("&&&&&&",emails,message)
    print("Email Sent!!!!!!!!!!!!!")
    

automatic_email()
