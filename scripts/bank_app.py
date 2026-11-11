from VD_games.bank.account import BankAccount, Bank

def print_menu():
    print("=" * 40)
    print("           БАНКОВСКАЯ СИСТЕМА")
    print("=" * 40)
    print("1. Открыть новый счёт")
    print("2. Пополнить счёт")
    print("3. Снять средства")
    print("4. Перевести средства")
    print("5. Показать баланс")
    print("6. Показать информацию о счёте")
    print("7. Список всех счетов")
    print("8. История операций по счету")
    print("0. Выход")
    print("=" * 40)

def get_current_account():
    acc_num = input("Введите номер вашего счета: ").strip()
    account = BankAccount.find_account(acc_num)
    if not account:
        print("Счет не найден!")
    return account

def main():
    while True:
        print_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            name = input("Введите ФИО владельца: ").strip()
            try:
                initial_balance = float(input("Введите начальный баланс (0, если нет): ") or 0)
            except ValueError:
                initial_balance = 0
            acc = BankAccount(name, initial_balance)
            print(f"Успешно! Ваш номер счета: {acc.account_number}")

        elif choice == "2":
            acc = get_current_account()
            if acc:
                try:
                    amount = float(input("Сумма пополнения: "))
                    acc.deposit(amount)
                except ValueError:
                    print("Ошибка: Введите число.")

        elif choice == "3":
            acc = get_current_account()
            if acc:
                try:
                    amount = float(input("Сумма снятия: "))
                    acc.withdraw(amount)
                except ValueError:
                    print("Ошибка: Введите число.")

        elif choice == "4":
            try:
                from_acc = input("Введите номер счета отправителя: ").strip()
                to_acc = input("Введите номер счета получателя: ").strip()
                amount = float(input("Сумма перевода: "))
                Bank.transfer(from_acc, to_acc, amount)
            except ValueError:
                print("Ошибка: Введите корректные данные.")

        elif choice == "5":
            acc = get_current_account()
            if acc:
                print(f"Ваш баланс: {acc.balance} руб.")

        elif choice == "6":
            acc = get_current_account()
            if acc:
                acc.get_account_info()

        elif choice == "7":
            BankAccount.list_all_accounts()

        elif choice == "8":
            acc = get_current_account()
            if acc:
                acc.show_history()

        elif choice == "0":
            print("Выход из системы. До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

        input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()
