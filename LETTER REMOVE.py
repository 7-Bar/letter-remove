def remove(text, oper, letter):
    if oper == "space":
        result = text.replace(" ","")
    elif oper == "letter":
        result = text.replace(letter, "")
    return result

while True:
    text = str(input("Enter full text: "))
    print()
    print("operation type: space or letter")
    oper_type = str(input("Enter the operation type: "))
    print()
    print("letter: ignore if oper type is space")
    letter = str(input("Enter the letter or phase: "))
    print()
    print(remove(text, oper_type, letter))
    print()
    respond = str(input("Enter [Y] if you want to quit: "))
    print()
    respond = respond.lower()
    if respond == "y":
        break