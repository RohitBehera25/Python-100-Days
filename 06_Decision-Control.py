email = input("Enter Your Email : ")

if "@" in email:
    password = input("Enter Your Password : ")

    if email == "rohit@gmail.com" and  password == "12345" :
        print("Welcome")
    elif email == "rohit@gmail.com" and password != "12345" :
        print("Password Not match")
        password = input("Enter Correct Password : ")
        if password == "12345":
            print("Password Match")
        else: 
            print("Still InCorrect")
    else:
        print("Invalid Credentials")
else: 
    print("Enter The Valid Email Id")


