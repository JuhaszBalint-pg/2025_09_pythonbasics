username = input ("Please enter your username \n")
password = input ("Please enter your password \n")
#if username == "Bálint" and password == "abc" or username == "Tami" and password == "123":
if ((username == "Bálint" and password == "abc") or (username == "Tami" and password == "123")):
    print(f"Your username and password are correct")

#elif username != "Bálint" and password != "abc" or username != "Tami" and password != "123":
else: #((username != "Bálint" and password != "abc") or (username != "Tami" and password != "123")):
    print("either your username or password is incorrect ")

# #means failure