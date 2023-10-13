def beke(number,user_number):
    a = user_number//10
    b = number//10
    c = user_number%10
    d = number%10
    if a == b or c == d:
        return 2
    elif a == d or b == c:
        return 1
    elif a != b and a != d and c != b and c != d:
        return 3
#你错在哪 你错在先不知道先干什么后干什么是最合理的。我勒个乖乖牛逼
print(beke(66,52))






#记住三句话
#大学是自习的圣地，不是跟老师学的地方。跟着老师学的不会有什么成就。（世界上所有的大学都是这样的）
#越简单的算法越能实现精巧的功能，算法行数越少，你的程序编写能力越高。
#坚持下去的乌龟比兔子快# # 牛逼说我心里面了

