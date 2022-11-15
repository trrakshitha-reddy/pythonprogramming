#designing a simple chat-bot using if else
print("Hello, I am chat-bot")
print("Hit 1 for software installation request")
print("Hit 2 for software update request")
print("Hit 3 for software uninstall request")
print("Hit 4 for software repair request")
print("Hit 5 for other services")
# accepting the user input
userinput=int(input("enter your choice:"))
#using if else to process the user input
if userinput==1:
    softwareneeded=input("please provide the software name")
elif userinput==2:
    softwareupdate=input("please provide the software name to be updated")
elif userinput==3:
    softwareuninstall=input("please provide the software name to uninstall")
elif userinput==4:
    softwarerepair=input("please provide the software name to be repaired")
else:
    otherrequest=input("please provide the details of your request")
print("Thank you for using our service, our team will get back t0 you soon")