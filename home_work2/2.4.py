text_4a = str(input("write 1st text: "))
text_4b = str(input("write 2nd text: "))
text_4c = str(input("write 3rd text: "))

if text_4a.isdigit():
    print( "Yes")
else:
    print("No")

if text_4b.isalpha():
    print( "Yes")
else:
    print("No")

print(text_4c.strip())


