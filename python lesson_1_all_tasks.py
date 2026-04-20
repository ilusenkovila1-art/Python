def task_1_create_variable():
    """Задание 1: Создание переменной."""
    print("=== Задание 1: Создание переменной ===")
    my_name = "Иван"  # Замените на ваше имя
    print(f"Значение переменной my_name: {my_name}")
    print()


def task_2_reassign_variable():
    """Задание 2: Перезапись переменной."""
    print("=== Задание 2: Перезапись переменной ===")
    my_age = 25  # Замените на ваш текущий возраст
    print(f"Текущий возраст: {my_age}")
    my_age = my_age + 3  # Возраст через три года
    print(f"Возраст через три года: {my_age}")
    print()


def task_3_user_input():
    """Задание 3: Получение пользовательского ввода."""
    print("=== Задание 3: Получение пользовательского ввода ===")
    print("Введите ваши данные:")
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    print(f"Вас зовут: {last_name} {first_name}")
    print()


def task_4_create_function():
    """Задание 4: Создание функции."""
    print("=== Задание 4: Создание функции ===")

    def print_greeting():
        """Функция выводит приветствие на экран."""
        print("Привет, мир!")

    print_greeting()
    print()


def task_5_function_parameterization():
    """Задание 5: Параметризация функций."""
    print("=== Задание 5: Параметризация функций ===")

    def print_number(num):
        """Функция выводит переданный номер на экран."""
        print(num, end='')

    # Вызов функции 11 раз для вывода номера 88005553535
    print("Вывод номера 88005553535:")
    digits = [8, 8, 0, 0, 5, 5, 5, 3, 5, 3, 5]
    
    for digit in digits:
        print_number(digit)
    
    print()  # Перевод строки после вывода
    print()


def main():
    """Основная функция для запуска всех заданий."""
    print("=" * 50)
    print("ВЫПОЛНЕНИЕ ЗАДАНИЙ УРОКА 1")
    print("=" * 50)
    print()

    # Выполнение всех заданий
    task_1_create_variable()
    task_2_reassign_variable()
    task_3_user_input()
    task_4_create_function()
    task_5_function_parameterization()

    print("=" * 50)
    print("ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ!")
    print("=" * 50)


if __name__ == "__main__":
    main()
