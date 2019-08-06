charac=input("enter a character:")
l=['a','e','i','o','u']
m=['!','@','$','%','^','&','*','(',')',"#"]
#if charac.isdigit=="false":
    #print("invalid")
#if charac.isalpha=="true":
if charac in l:
    print("vowel")
elif charac in m:
    print("invalid")
else:
    print("consonant")

#else:
 #   print("invalidd")