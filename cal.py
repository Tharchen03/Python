while True:
    operation = input(
        "what kind of operation u want to do?(add,sub,mul,div or exit): ")

    if operation == "exit":
        print("Exiting...")
        break

    try:
        a = int(input("1st num: "))
        b = int(input("2nd num: "))

        if operation == "add":
            add = a + b
            print("Sum: " +str(add))
        elif operation == "sub":
            sub = a-b
            print("differences: " +str(sub))

        elif operation == "mul":
            mul = a*b
            print("mul: " +str(mul))
        elif operation == "div":
            div = a/b
            print("div: " +str(div))
        else:
            print("Invalid Operation ")
    except ValueError:
        print("Invalid input, please enter a valid number")




