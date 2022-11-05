# write your code here
operations = ["+", "-", "*", "/"]
memory = 0


def check_input():
    calc = input("Enter an equation\n")
    calc_var = calc.split(" ")
    if calc_var[0].lower() == 'm':
        calc_var[0] = memory
    if calc_var[2].lower() == 'm':
        calc_var[2] = memory
    try:
        first_number = float(calc_var[0])
        second_number = float(calc_var[2])
        if calc_var[1] in operations:
            return list([first_number, second_number, calc_var[1]])
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            return check_input()
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        return check_input()


def do_the_math(data):
    check_digit_length(data)
    if data[-1] == '+':
        return data[0] + data[1]
    elif data[-1] == '-':
        return data[0] - data[1]
    elif data[-1] == '*':
        return data[0] * data[1]
    elif data[-1] == '/' and data[1] != 0:
        return data[0] / data[1]
    elif data[-1] == '/' and data[1] == 0:
        print("Yeah... division by zero. Smart move...")
        return do_the_math(check_input())


def save_data(math_result):
    global memory
    mesages = ["Are you sure? It is only one digit! (y / n)\n",
               "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
               "Last chance! Do you really want to embarrass yourself? (y / n)\n"]

    answer = input("Do you want to store the result? (y / n):\n")
    if answer.lower() == "y" and is_one_digit(math_result):
        counter = 0
        while counter < 3:
            tries = input(mesages[counter])
            if tries.lower() == "n":
                break
            else:
                counter += 1
        if counter == 3:
            memory = math_result
    elif answer.lower() == "y":
        memory = math_result


def check_digit_length(data):
    msg = [" ... lazy", " ... very lazy", " ... very, very lazy", "You are"]
    final_message = ""
    if is_one_digit(data[0]) and is_one_digit(data[1]):
        final_message += msg[0]
    if (data[0] == 1 or data[1] == 1) and data[2] == "*":
        final_message += msg[1]
    if (data[0] == 0 or data[1] == 0) and (data[2] in ("*", "+", "-")):
        final_message += msg[2]
    if final_message != "":
        final_message = msg[3] + final_message
    print(final_message)


def is_one_digit(x):
    if -10 < x < 10 and x.is_integer():
        return True
    return False


while True:
    equation_result = do_the_math(check_input())
    print(equation_result)
    save_data(equation_result)
    if input("Do you want to continue calculations? (y / n):\n").lower() != 'y':
        break
