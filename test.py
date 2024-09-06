def main(input_str: str):
    elements = input_str.split()
    if len(elements) !=3:
        return ("throws Exception //т.к. формат математической операции \
                 не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
    try:
        a = int(elements[0])
        b = int(elements[2])
        if not 1<= a <=10:
            raise ("Один из операндов не входит в диапозон от 1 до 10")
        if not 1<= b <=10:
            raise ("Один из операндов не входит в диапозон от 1 до 10")
        if elements[1] == '+':
            result = a + b
        if elements[1] == '-':
            result = a - b
        if elements[1] == '*':
            result = a * b
        if elements[1] == '/':
            result = a // b
        return str(result)
    except IndexError as e:
        print(type(e))
        print("throws Exception //т.к. строка не является математической операцией")
    except TypeError as e:
        print(type(e))
        print("Операнд не входит в диапозон от 1 до 10")
        return str(e)

while True:
    primer = input("Введите пример в формате '2 + 4':")
    if primer.lower() == 'exit':
        break

    result = main(primer)
    print(result)



