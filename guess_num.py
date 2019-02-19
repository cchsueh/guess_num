import random

r = random.randint(1, 100)
print('猜數字遊戲')
print('遊戲開始!!')

while True:
    user_unm = input('請輸入數字：')
    user_unm = int(user_unm)
    if user_unm == r:
        print('答對，答案為：', r)
        print('遊戲結束!!')
        break
    elif user_unm > r:
        print('比答案大，請重猜一次!!')
    elif user_unm < r:
        print('比答案小，請重猜一次!!')