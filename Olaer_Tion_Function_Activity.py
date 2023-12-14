def main():
    while True:
        try:
            print("")
            num1 = int(input("Enter 1st integer: "))
            num2 = int(input("Enter 2nd integer: "))
            num3 = int(input("Enter 3rd integer: "))
            logic(num1, num2, num3)
            again()
        except ValueError:
            print("Enter a valid integer")


def logic(num1, num2, num3):
    if num1 == num2 == num3:
        answer = num1 * num2 * num3
    elif num1 == num3:
        answer = num1 * num3 + num2
    elif num1 == num2:
        answer = num1 * num2 + num3
    elif num2 == num3:
        answer = num2 * num3 + num1
    else:
        answer = num1 + num2 + num3
    print("The answer is:", answer)


def again():
    while True:
        try:
            response = input("\nDo you want to enter another?(yes/no): ").lower()
            if response != 'yes':
                print("\nProgram Terminated")
                exit()
            else:
                main()
        except ValueError:
            print("error")


main()
