def fun_string(message:str, option:str):
    if option == "find":
        sign = str(input("what do you want to find? "))
        return message.find(sign)+1
    elif option == "count":
        sign = str(input("what do you want to count? "))
        return message.count(sign)
    elif option == "replace":
        sign = str(input("what do you want to replace? "))
        change_sign = str(input("what do you want to change to? "))
        return message.replace(sign, change_sign)

message = str(input("write your message: "))
option = str(input("choose option: find, count, replace: ")).lower()
print(fun_string(message, option))

