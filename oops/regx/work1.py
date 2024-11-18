import re
password='^[A-Z][a-zA-Z0-9!@#$%^&*-+?/]{7}$'
user=input("enter you password:")
if re.search(password,user):
    print("valid password")
else:
    print("invalid password")