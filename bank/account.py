import random

class BankAccount:
    all_accounts = {}

    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_number = str(random.randint(1000, 9999))
        
        self.history = []
        self._add_to_history(f"Открытие счета с балансом {initial_balance} руб.")

        while self.account_number in BankAccount.all_accounts:
            self.account_number = str(random.randint(1000, 9999))
        BankAccount.all_accounts[self.account_number] = self

    def _add_to_history(self, message):
        self.history.append(message)

    def deposit(self, amount):
        if amount <= 0:
            print("Ошибка: Сумма должна быть больше нуля.")
            return
        if amount > 50000:
            print("Ошибка: Максимальная сумма пополнения — 50000.")
            return
        self.balance += amount
        msg = f"Пополнение на {amount} руб. Баланс: {self.balance} руб."
        print(msg)
        self._add_to_history(msg)

    def withdraw(self, amount):
        if amount <= 0:
            print("Ошибка: Сумма должна быть больше нуля.")
            return
        if amount > 50000:
            print("Ошибка: Максимальная сумма снятия — 50000.")
            return
        if amount > self.balance:
            print(f"Ошибка: Недостаточно средств. Ваш баланс: {self.balance} руб.")
            return
        self.balance -= amount
        msg = f"Снятие {amount} руб. Баланс: {self.balance} руб."
        print(msg)
        self._add_to_history(msg)

    def get_owner_info(self):
        print(f"Владелец: {self.owner_name} | Счет: {self.account_number} | Баланс: {self.balance} руб.")

    def get_account_info(self):
        print(f"--- Информация о счете ---")
        print(f"Номер счета: {self.account_number}")
        print(f"Владелец: {self.owner_name}")
        print(f"Баланс: {self.balance} руб.")
        print(f"--------------------------")

    def show_history(self):
        print(f"\n--- История операций по счету {self.account_number} ---")
        if not self.history:
            print("Операций пока не было.")
        for operation in self.history:
            print(f"- {operation}")
        print("--------------------------------------------------\n")

    @classmethod
    def find_account(cls, account_number):
        return cls.all_accounts.get(account_number)

    @classmethod
    def list_all_accounts(cls):
        if not cls.all_accounts:
            print("В системе пока нет открытых счетов.")
            return
        print("\n--- Список всех счетов ---")
        for acc_num, acc in cls.all_accounts.items():
            print(f"Счет: {acc_num} | Владелец: {acc.owner_name} | Баланс: {acc.balance} руб.")
        print("---------------------------\n")


class Bank:
    
    @staticmethod
    def transfer(from_account_num, to_account_num, amount):
        if amount <= 0:
            print("Ошибка: Сумма перевода должна быть больше нуля.")
            return
        if amount > 20000:
            print("Ошибка: Максимальная сумма перевода — 20000.")
            return
            
        sender = BankAccount.find_account(from_account_num)
        receiver = BankAccount.find_account(to_account_num)

        if not sender:
            print(f"Ошибка: Счет отправителя {from_account_num} не найден.")
            return
        if not receiver:
            print(f"Ошибка: Счет получателя {to_account_num} не найден.")
            return
        if sender == receiver:
            print("Ошибка: Нельзя перевести средства на тот же счет.")
            return
        if amount > sender.balance:
            print(f"Ошибка: Недостаточно средств. Баланс отправителя: {sender.balance} руб.")
            return

        sender.balance -= amount
        receiver.balance += amount

        msg_sender = f"Перевод {amount} руб. на счет {to_account_num}. Баланс: {sender.balance} руб."
        msg_receiver = f"Получен перевод {amount} руб. от счета {from_account_num}. Баланс: {receiver.balance} руб."
        
        sender._add_to_history(msg_sender)
        receiver._add_to_history(msg_receiver)

        print(f"Успешно! Переведено {amount} руб. со счета {from_account_num} на счет {to_account_num}.")
