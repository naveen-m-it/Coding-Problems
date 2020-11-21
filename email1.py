'''this is created by Naveen'''
#to import smtplib this is used to connect to the mail protocol

import smtplib

#this is a sample method for working sample
#use your email and default password to send mail
sender = ("example@gmail.com")
recv = input("Enter email to send:")
message=input("Enter message:")
pas = input("enter password:")

#there is i use gmail smtp you also using other company smtps for other email 

s = smtplib.SMTP('smtp.gmail.com',587)

#start tls is starting tls for login your account
s.starttls()

#this login your accound and password
s.login(sender,pas)

#this method checks email sent or not
try:
    s.sendmail(sender,recv,message)
    print("mail sent successfully")
except:
    print("mail not send")
s.quit()#close the program
