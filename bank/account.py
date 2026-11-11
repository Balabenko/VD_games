import random

class BankAccount:
    all_accounts = {}

    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_number = str(random.randint(1000, 9999))
        
        while self.account_number in BankAccount.all_accounts:
            self.account_number = str(random.randint(1000, 9999))
        BankAccount.all_accounts[self.account_number] = self

    def deposit(self, amount):
        if amount > 50000:
            print(f"Ошибка: Максимальная сумма пополнения — 50000. Вы пытались внести {amount}.")
            return
        self.balance += amount
        print(f"Пополнение на {amount} руб. Баланс: {self.balance} руб.")

    def withdraw(self, amount):
        if amount > 50000:
            print(f"Ошибка: Максимальная сумма снятия — 50000. Вы пытались снять {amount}.")
            return
        if amount > self.balance:
            print(f"Ошибка: Недостаточно средств. Ваш баланс: {self.balance} руб.")
            return
        self.balance -= amount
        print(f"Снятие {amount} руб. Баланс: {self.balance} руб.")

    def get_owner_info(self):
        print(f"Владелец: {self.owner_name} | Счет: {self.account_number} | Баланс: {self.balance} руб.")

    def transfer(self, target_account_number, amount):
        """Перевод с одного счета на другой (макс. 20000)."""
        if amount > 20000:
            print(f"Ошибка: Максимальная сумма перевода — 20000. Вы пытались перевести {amount}.")
            return
        if amount > self.balance:
            print(f"Ошибка: Недостаточно средств для перевода. Ваш баланс: {self.balance} руб.")
            return
        
        target_account = BankAccount.all_accounts.get(target_account_number)
        if not target_account:
            print(f"Ошибка: Счет с номером {target_account_number} не найден.")
            return
        if target_account == self:
            print("Ошибка: Нельзя перевести средства на тот же счет.")
            return

        self.balance -= amount
        target_account.balance += amount
        print(f"Перевод {amount} руб. на счет {target_account_number} выполнен.")
        print(f"Ваш новый баланс: {self.balance} руб.")

    def get_account_info(self):
        print(f"--- Информация о счете ---")
        print(f"Номер счета: {self.account_number}")
        print(f"Владелец: {self.owner_name}")
        print(f"Баланс: {self.balance} руб.")
        print(f"--------------------------")

    @classmethod
    def list_all_accounts(cls):
        if not cls.all_accounts:
            print("В системе пока нет открытых счетов.")
            return
        
        print("\n--- Список всех счетов ---")
        for acc_num, acc in cls.all_accounts.items():
            print(f"Счет: {acc_num} | Владелец: {acc.owner_name} | Баланс: {acc.balance} руб.")
        print("---------------------------\n")
