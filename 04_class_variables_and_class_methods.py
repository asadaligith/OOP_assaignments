class Bank:
  bank_name = "NBP"

  def __init__(self, cus_name):
    self.cus_name = cus_name

  @classmethod
  def change_bank_name(cls, name):
    cls.bank_name = name

  def show_bank_name(self):
    print(f"{self.cus_name} Current Account in Bank {Bank.bank_name}")

acc1 = Bank("Asad")
acc2 = Bank("Ali")

acc1.show_bank_name()
acc2.show_bank_name()

Bank.change_bank_name("Meezan")

acc1.show_bank_name()
acc2.show_bank_name()
