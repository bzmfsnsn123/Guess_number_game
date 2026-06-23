import random
def guess_number():
    answer=random.randint(1,100)
    count=0
    print("=====猜数字游戏=====")
    print("系统生成了一个1-100的数字，快来猜一猜吧！")

    while True:
       try:
          guess=int(input("请输入你猜的数字"))
          count +=1

          if guess >answer :
              print("猜大了，往小猜一下试试")

          elif guess<answer:
              print("猜小了，往大猜一下")
          else:
              print(f"恭喜你,猜对了，答案就是{answer}")
              print(f"你一共猜了{count}次，好厉害哦")
              break

       except ValueError:
           print("闹呢，请输入合法数字😶")

if __name__=="__main__":
    guess_number()



