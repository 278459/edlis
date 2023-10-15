'''
Project:图书馆书籍管理
Project description:小明开了一架图书馆，现在急需搭建一个图书管理系统。该系统要实现：
图书添加删除，图书进货卖出，购书信息等功能。
开发两个类，第一个类是图书类，有图书的信息（图书名，作者，售价，
库存数量等）变量，可以实现库存数的更改等功能。第二个类是借书信息类，有购书信息（购
书人姓名，支付方式，买的书等。），可以实现添加借书信息等功能。
'''


class Book:
    def __int__(self, name, writer, price, number):
        self.name = name
        self.writer = writer
        self.price = price
        self.number = number

    def updata_number(self, change_number):
        self.number += change_number


class Buy_formation:
    def __int__(self, buy_name, pay_method, buy_book):
        self.buy_name = buy_name
        self.pay_method = pay_method
        self.buy_book = buy_book

    def add_borrow_info(self,buy_name, pay_method, buy_book):
        new_borrow_info = Buy_formation(buy_name, pay_method, buy_book)
        return new_borrow_info









