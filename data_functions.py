from operators import Addition, Multiplication, Division



def input_complex_number(n): # Функция для ввода пользователем комплексного числа.
    
    print(f"Введите {n} комплексное число")
    real = float(input("Введите действительную часть: "))
    imag = float(input("Введите мнимую часть: "))
    return complex(real, imag)


def input_operation(math_action):
    if math_action == "+":
        print(f"Введён оператор: {math_action}")
        return Addition()
    elif math_action == "*":
        print(f"Введён оператор: {math_action}")
        return Multiplication()
    elif math_action == "/":
        print(f"Введён оператор: {math_action}")
        return Division()
    else:
        print(f"ОШИБОЧНО введён оператор: {math_action}")
        return input_operation(input("Неверное значение. Введите одну из операций:+,*,/"))