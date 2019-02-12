from symbols import lowercase, uppercase


str = "A123"
found_a_variable = False
for item in uppercase:
    if item in str:
        found_a_variable = True

if found_a_variable:
    print("algebraic expression")

else:
    print("This can be rewritten or calculated:")
    choice = input("Do you want to rewrite this expression or calculate it: ")

    if choice == "calculate":
        print("Calculating now")

    elif choice == "rewrite":
        print("Rewritting it")

    else:
        print("I didn't quite understand, please repeat that")