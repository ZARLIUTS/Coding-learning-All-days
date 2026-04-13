import random

lucky_number= random.randint(1,10)

while True:
    guess = int(input("enter number:"))
    if guess == lucky_number:
        print("ถั่วต้มแร้ว, สวดยอด")
        break  # ทายถูกแล้วออกจากลูป
    elif guess > lucky_number:
        print("โอโห, เยอะไปไก่งะ")
    else:
        print("น้อยไป ไปๆ พอเถอะ")