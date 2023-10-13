#判断输入的文本是否全英文（包括符号）
def all_english(text):
    libs = []
    for i in range(32, 127):
        libs.append(chr(i))
    for i in text:
        if i not in libs:
            return False
    return True

def main():
    print("Welcome to English Only")
    #众所周知，While sth.是循环函数，While True啥意思，就是无限循环
    while True:
        msg = input("Enter some English:")
        if all_english(msg):
            print("Wonderful!ALl words are Englsih!")
        else:
            print("Wait!Something is not English!")
            #就是这么简单。
    #你看通过你的函数，我制作程序多么方便

#这里的Main（）就是让程序进入main函数来执行入口，main又被称为入口函数。
#你如果扮演我这个程序员，你也要制作入口函数，入口函数就是直接与用户交互的函数
#allenglish函数你可以叫它....幕后函数吧，哈哈，虽然在幕后，但是大部分的工作都是它来承担的。
#下面我将演示一直判断。你可以学习一下
#我六点要出图书管，时间够不。我天，3分钟就解决的事。牛逼
main()