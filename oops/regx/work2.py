import re
email='[a-zA-Z0-9]+@gmail.com$'
user=input("enter you email:")
if re.search(email,user):
    print("valid email")
else:
    print("invalid email")   