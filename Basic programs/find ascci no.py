

chr=(input("Enter a character"))
x=ord(chr)

if x>=65 and x<=90:
    print("Capital letter")
elif x>=97 and x<=122:
    print("Small letter")
elif x>=48 and x<=57:
    print("it is a digit")
else:
    print("the char is invalid")