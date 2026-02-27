import random

answer = random.randint(1, 10)

for i in range(3):
    guess = int(input("1〜10の数字を当ててください: "))

    if guess > answer:
        print("もっと小さいよ")
    elif guess < answer:
        print("もっと大きいよ")
    else:
        print("正解!")
        break
else:
    print("不正解… 正解は" , answer , "でした")