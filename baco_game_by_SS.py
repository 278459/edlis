def baco(number,user_number,bit):
    #bit是输入的数字位数
    s_num=str(number)#将输入参数（系统随机生成）变为字符串
    u_num=str(user_number)#as above
    #化成字符串的原因是只有字符串才能进行数组操作（列表类YES）
    for i in range(0,bit):#对用户输入的数字逐个查验,i分别从0开始一直到bit前面的数字（注意索引从0开始哈有什么不懂得都可以问）
        if u_num[i] == s_num[i]:#数字相同且位置相同
            return 2
        #假如只循环一次，在这里判断。那么假如说
        #系统生成的是236  用户输入的是326.
        #从用户输入的3开始判断，发现不符合判断的条件，于是进入elif，我累乖乖懂了
        #我以后还是多相信我的第一反应吧哈哈哈哈，两个脑子打架刚才。牛逼，我去上个厕所（小的）憋一个小时了，你的信息灌输让我忘却膀胱的胀感，太美妙了，牛逼毁了，我累乖乖，一上厕所发现五楼加上我就两个男的牛逼！
    for i in range(0, bit):
        if u_num[i] in s_num:
            return 1
    return 3
#你错在哪 你错在先不知道先干什么后干什么是最合理的。我勒个乖乖牛逼
print(baco(6666666666,5261235412,10))
#如果输入的2位数，跟刚才一样，下面我要输入3位数了
#OK，我宣布：本项目结束我再看一遍OK
#我的算法比你的长，但是我这个算法有一个极大的好处，你准备好看了吗？yes
#怎么样我类个乖乖，还得是顺，牛逼毁了。你可以输入10位数。



#记住三句话
#大学是自习的圣地，不是跟老师学的地方。跟着老师学的不会有什么成就。（世界上所有的大学都是这样的）
#越简单的算法越能实现精巧的功能，算法行数越少，你的程序编写能力越高。
#坚持下去的乌龟比兔子快# # 牛逼说我心里面了
import random
def main():
    #既然都到这个份了，那就三位数了
    s_n=random.randint(100,999)
    print("Welcome to Baco game")
    print("We have thought a 3-bit number,guess it!")
    while True:
        u_n=input("Enter your answer:")
        return_nu=baco(s_n,u_n,3)
        if return_nu==1:
            print("You have number(s) right but in wrong position.")
        elif return_nu==2:
            print("You have number(s) right and in correct position.")
        elif return_nu==3:
            print("You have NO number(s) right and in correct position.")
        else:
            print('Fuck you,Error!')
    #嘿嘿，忘了加用户如果猜对的情况了，没事，就这样吧。
main()
#就这样吧，训练为主，游戏不好玩。nb