import random

r = random.randint(1, 100)
count = 0
print('猜數字遊戲')
print('遊戲開始!!')

while True:
    count += 1
    user_unm = input('請輸入數字：')
    user_unm = int(user_unm)
    if user_unm == r:
        print('答對，答案為：', r)
        print('遊戲結束!!')
        print('已經猜了', count, '次')
        break
    elif user_unm > r:
        print('比答案大，請重猜一次!!')
    elif user_unm < r:
        print('比答案小，請重猜一次!!')
    print('已經猜了', count, '次')