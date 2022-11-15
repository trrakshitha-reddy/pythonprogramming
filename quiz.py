#design a quize application using the concept of conditionals
print("welcome to the quize")
player=input("are you intrested to play? ")
if player!="yes":
    quit()
else:
    print("okay! lets begin with the first question")
answer=input("PESITM Shivamogga is located in karnataka? true or false ")
if answer=="true":
    print('correct answer')
else:
    print('Incorrect answer')
answer=input("What does CPU stands for? a)Control Processing Unit b)central processing unit ")
if answer=="a":
    print('Incorrect')
else:
    print('yes, correct answer. It is central processing unit')
answer=input("Shivamogga is called the Capital of Malnadu. True or false ")
if answer=="True":
    print('Correct answer')
else:
    print('Incorrect answer')
answer=input("How many departments are there in the PESITM?  a)5 b)7 c)9 ")
if answer=="a":
    print('Incorrect, there are 7 departments in the PESITM')
elif answer=="c":
    print('Incorrect, there are 7 departments in the PESITM')
else:
    print('Correct answer')
answer=input("Pointer is a special variable. True or false s")
if answer=="True":
    print('Correct answer')
else:
    print('Incorrect, pointer is a special variable used to store the address of another variable')
print("Thank you for attending the quize. We will send your score to your mail")