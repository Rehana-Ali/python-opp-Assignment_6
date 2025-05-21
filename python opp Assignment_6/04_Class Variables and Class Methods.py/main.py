class Bank:
    bank_name = "Bank ABC"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
 
user1 = Bank()
print("before changing bank name")
print(f"user's 1 bank name is  {user1.bank_name}")

Bank.change_bank_name("Bank xyz")
print("After changing name")

print(f"user's 1 bank name is  {user1.bank_name}")