import re
txt=raw_input("enter a value:")
x=re.search("\d\d\d-\d\d-\d\d\d\d", txt) 
if (x):
    print("matching")
else:
    print("Not matching")
