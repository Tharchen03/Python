while True:
    num = input("What operation do you want to do? (add, sub, mul, div, or exit): ")

    if num == "exit":
        print("Exiting...")
        break

    try:
        a = int(input("First number: "))
        b = int(input("Second number: "))

        if num == "add":
            sum1 = a+b
            print("Sum: " + str(sum1))
        elif num == "sub":
            sub = a-b
            print("Difference: " + str(sub))
        elif num == "div":
            div = a/b
            print("Quotient: " + str(div))
        elif num == "mul":
            mul = a*b
            print("Product: " + str(mul))
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid input, please enter a valid number")
