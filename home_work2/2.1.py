def string_change(message:str, option:str):
    if option == "upper":
        return message.upper()
    elif option == "lower":
        return message.lower()
    elif option == "standart":
        return message.capitalize()



message = str(input())
print("options: upper, lower, standart")
option = str(input()).lower()
print(string_change(message, option))