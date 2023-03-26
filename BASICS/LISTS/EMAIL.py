import re
mail=input("enter:")
if re.match('^[a-zA-Z0-9]*[@][a-zA-Z]*[.][a-zA-Z]{2,3}$',mail):
    print("matched")
else:
    print("not matched")