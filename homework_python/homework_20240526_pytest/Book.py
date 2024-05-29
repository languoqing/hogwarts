import os


class Book(object):
    def __init__(self, bid, name, price, summary):
        self.bid = bid
        self.name = name
        self.price = price
        self.summary = summary

    # 重写对象的显示格式 方法
    def __str__(self):
        return f"BID: {self.bid} --- Name: {self.name} --- Price: {self.price} --- Summary: {self.summary}"


# 封装管理类
class BookManagement(object):
    def __init__(self):
        # 定义一个全局变量，用来保存图书的信息，方法各个方法之间进行访问
        self.books = []
        self.load_data()

    # 菜单方法
    def __menu(self):
        print("****************************************")
        print("*                图书管理系统           *")
        print("*        1. 添加新图书信息              *")
        print("*        2. 通过图书编号修改图书信息        *")
        print("*        3. 通过图书编号删除图书信息        *")
        print("*        4. 通过图书名称删除图书信息        *")
        print("*        5. 通过图书编号查询图书信息        *")
        print("*        6. 通过图书名称查询图书信息        *")
        print("*        7. 显示所有图书信息            *")
        print("*        8. 退出系统                   *")
        print("****************************************")
        select_op = input("输入编号选择操作：")
        return select_op

    # 获取图书编号
    def __getBid(self):
        bid = input("请输入图书ID:")
        return bid

    # 获取名称
    def __getName(self):
        name = input("请输入图书名称：")
        return name

    # 获取价格
    def __getPrice(self):
        while True:
            price = input("请输入图书价格：")
            if price.isdigit():
                return int(price)
            else:
                print("输入价格不合法，请输入数字")

    # 获取简介
    def __getSummary(self):
        summary = input("请输入图书简介：")
        return summary

    # 添加图书
    def addBook(self, bid, name, price, summary):
        for s in self.books:
            if s.bid == bid:
                print("图书编号已存在，添加失败")
                return "添加失败"
        else:
            book = Book(bid, name, price, summary)
            self.books.append(book)
            print("添加图书信息成功")
            return '添加成功'

    # 通过图书编号修改图书信息
    def modifyBookByID(self, bid, name, price, summary):
        for s in self.books:
            if s.bid == bid:
                s.name = name
                s.price = price
                s.summary = summary
                print("修改成功")
                return "修改成功"
        else:
            print(f'没有 {bid} 对应的图书信息')
            return "修改失败"

    # 通过ID删除图书信息
    def deleteBookByID(self, bid):
        for s in self.books:
            if s.bid == bid:
                self.books.remove(s)
                print("删除成功")
                return "删除成功"
        else:
            print(f'没有 {bid} 对应的图书信息')
            return "删除失败"

    # 通过图书名称 删除所有符合的图书
    def deleteBookByName(self, name):
        exist_s = []
        # 找出所有要删除的图书
        for s in self.books:
            if s.name == name:
                exist_s.append(s)

        # 开始删除
        if len(exist_s) > 0:
            for s in exist_s:
                self.books.remove(s)
                print(f"名称为 { name } 的图书删除成功")
            else:
                print(f"成功删除 {len(exist_s)} 个图书")
                return "删除成功"
        else:
            print(f"图书【{name}】不存在，无法删除")
            return "删除失败"

    # 通过图书编号查询图书信息
    def queryBookByID(self, bid):
        for s in self.books:
            if s.bid == bid:
                print(f"图书编号 {bid} 的图书信息如下：")
                print(s)
                return "查询成功"
        else:
            print(f"图书编号 {bid} 的图书不存在")
            return "查询失败"

    # 通过名称查询图书信息
    def queryBookByName(self, name):
        result = []
        for s in self.books:
            if s.name == name:
                result.append(s)

        if len(result) > 0:
            print(f"名称为 {name} 的图书共 {len(result)} 名，信息如下：")
            for s in result:
                print(s)
            return "查询成功"
        else:
            print(f"名称为 {name} 的图书不存在")
            return "查询失败"

    # 显示所有图书信息
    def __show(self):
        print("所有图书信息如下：")
        for s in self.books:
            print(s)

    # 加载文件
    def load_data(self):
        print("数据从文件加载完毕！！")
        # 判断文件是否存在
        if os.path.exists("books.txt"):
            with open("books.txt", "r") as file:
                content = file.read()
                content = content.split("\n")
                content.remove("")
                for line in content:
                    line = line.split("-")
                    book = {}
                    book["bid"] = line[0]
                    book["name"] = line[1]
                    book["price"] = int(line[2])
                    book["summary"] = line[3]
                    self.books.append(book)

    # 保存文件
    def save_data(self):
        print("将数据写入文件保存完毕！！")
        with open("books.txt", "w") as file:
            for book in self.books:
                # 使用 - 做为间隔符拼接所有的数据
                book = list(book.values())
                book = [str(el) for el in book]
                bookStr = "-".join(book) + '\n'
                file.write(bookStr)

    # 管理方法
    def manpricer(self):
        while True:
            select_op = self.__menu()
            if len(select_op) == 1 and select_op in "12345678":
                if select_op == "1":
                    bid = self.__getBid()
                    name = self.__getName()
                    price = self.__getPrice()
                    summary = self.__getSummary()
                    self.addBook(bid, name, price, summary)
                elif select_op =="2":
                    bid = self.__getBid()
                    name = self.__getName()
                    price = self.__getPrice()
                    summary = self.__getSummary()
                    self.modifyBookByID(bid, name, price, summary)
                elif select_op =="3":
                    bid = self.__getBid()
                    self.deleteBookByID(bid)
                elif select_op =="4":
                    name = self.__getName()
                    self.deleteBookByName(name)
                elif select_op =="5":
                    bid = self.__getBid()
                    self.queryBookByID(bid)
                elif select_op =="6":
                    name = self.__getName()
                    self.queryBookByName(name)
                elif select_op =="7":
                    self.__show()
                else:
                    self.save_data()
                    break
            else:
                print("输入的数据不合法，请输入在合法范围内的操作编号！！！")