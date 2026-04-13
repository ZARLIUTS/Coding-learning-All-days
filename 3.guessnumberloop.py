import random
lucky_number= random.randint(1,11)
while True:
    guess = int(input("enternumber"))

    lucky_number = random.randint(1, 10)
       print("ถั่วต้มแร้ว , สวดยอด")
       break
elif: guess > lucky_number:
    print("โอโห , ไก่งะ")
else:
    print("ไปไปพอเถอะ")