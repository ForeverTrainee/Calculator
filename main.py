def main():
    first_number = get_first_number()
    while True:

        operation = get_operation()
        second_number = get_second_number()
        if operation == "+":
            result = addition(first_number, second_number)
            print(result)
        if operation == "-":
            result = subtraction(first_number, second_number)
            print(result)
        if operation == "*":
            result = multiplication(first_number, second_number)
            print(result)
        if operation == "/":
            result = divsion(first_number, second_number)
            print(result)
        continue_operation = input(
            "Should continue with current number press y, or type n for new calculation "
        )
        if continue_operation == "y":
            first_number = result
        else:
            first_number = get_first_number()


def get_first_number():
    number = float(input("What`s the number? "))
    return number


def get_second_number():
    while True:
        try:
            number = float(input("What`s the number? "))
            return number
        except ValueError:
            pass


def get_operation():
    while True:
        try:
            print("+\n-\n*\n/\n")
            operation = input("Pick an operation: ")
            if (
                operation != "+"
                and operation != "-"
                and operation != "*"
                and operation != "/"
            ):
                pass
            else:
                return operation
        except ValueError:
            pass


def addition(arg, arg2):
    return arg + arg2


def subtraction(arg, arg2):
    return arg - arg2


def multiplication(arg, arg2):
    return arg * arg2


def divsion(arg, arg2):
    return arg / arg2


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
