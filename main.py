from data_functions import input_complex_number, input_operation
from calculate import ComplexCalculator


def main(): #Основная функция калькулятора комплексных чисел.
    print("Ввод первого комплексного числа:")
    num1 = input_complex_number(1)

    print("Ввод операции:+,*,/")
    operation = input_operation(input("Введите одну из операций:+,*,/"))

    print("Ввод второго комплексного числа:")
    num2 = input_complex_number(2)

    calculator = ComplexCalculator(operation)

    result = calculator.calculate(num1, num2)
    print(f"Вывод результата: {result}")

    print(f"Результат {calculator}: {result}")


if __name__ == "__main__":
    main()