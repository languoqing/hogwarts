
"""
作业地址：https://ceshiren.com/t/topic/31607
"""
import os.path

books = []
def menu():
    """菜单函数"""
    print("*****************************")
    print("*      图书管理系统           *")
    print("* 1. 添加新图书信息           *")
    print("* 2. 通过图书ID修改图书信息      *")
    print("* 3. 通过图书ID删除图书信息      *")
    print("* 4. 通过书名删除图书信息      *")
    print("* 5. 通过图书ID查询图书信息      *")
    print("* 6. 通过书名查询图书信息      *")
    print("* 7. 显示所有图书信息         *")
    print("* 8. 退出系统                *")
    print("*****************************")
    input_no = input("请输入用户编号：")
    return input_no

def book_manager():
    load_data()
    while True:
        input_no = menu()
        if input_no == '1':
            add_book(get_id(), get_name(), get_price(), get_summary())
        elif input_no == '2':
            modify_book_by_id(get_id())
        elif input_no == '3':
            delete_book_by_id(get_id())
        elif input_no == '4':
            delete_book_by_name(get_name())
        elif input_no == '5':
            query_book_by_id(get_id())
        elif input_no == '6':
            query_book_by_name(get_name())
        elif input_no == '7':
            show_all_info()
        elif input_no == '8':
            save_data()
            return
        else:
            print("输入不符合要求")
            break

def get_id():
    sid = input("请输入编号：")
    return sid

def get_name():
    name = input("请输入书名：")
    return name

def get_price():
    price = input("请输入价格：")
    return int(price)

def get_summary():
    summary = input("请输入简介：")
    return summary


def add_book(id, name, price, summary):
    book_dict = dict()
    book_dict['sid'] = id
    book_dict['name'] = name
    book_dict['price'] = price
    book_dict['summary'] = summary
    sids = [i.get('sid') for i in books]
    if id not in sids:
        books.append(book_dict)
        return "添加成功"
    return "添加失败"

def modify_book_by_id(id):
    for i in books:
        if id == i.get('sid'):
            i['name'] = get_name()
            i['price'] = get_price()
            i['summary'] = get_summary()
            return "修改成功"
    return "修改失败"

def delete_book_by_id(id):
    for i in books:
        if id == i.get('sid'):
            books.remove(i)
            return "删除成功"
    return "删除失败"

def delete_book_by_name(name):
    len_books = len(books)
    for i in books:
        if name == i.get('name'):
            books.remove(i)
    if len_books == len(books):
        return f"删除失败"
    return f"删除成功"

def query_book_by_id(id):
    for i in books:
        if id == i.get('sid'):
            print(f"sid:{i.get('sid')},name:{i.get('name')},price:{i.get('price')}, summary:{i.get('summary')}")
            return "查询成功 "
    return "查询失败"

def query_book_by_name(name):
    re_books = []
    for i in books:
        if name == i.get('name'):
            re_books.append(i)
    if len(re_books) > 0:
        for book in re_books:
            print(f"sid:{book.get('sid')},name:{book.get('name')},price:{book.get('price')}, summary:{book.get('summary')}")
        return "查询成功"
    return "查询失败"

def show_all_info():
    for i in books:
        print(f"sid:{i.get('sid')},name:{i.get('name')},price:{i.get('price')}, summary:{i.get('summary')}")


def save_data():
    with open('db.txt','w') as f:
        for i in books:
            a = []
            for k, v in i.items():
                 a.append(f"{k}:{v}-")
            f.write("".join(a)[:-1] + '\n')

def load_data():
    if os.path.exists('db.txt'):
        with open('db.txt', 'r') as f:
            re_file = f.read()
            re_l = re_file.split('\n')[:-1]
            print(f"re_l:{re_l}")
            for i in re_l:
                book = {}
                info = i.split('-')
                print(f"info:{info}")
                for a in info:
                    book_info = a.split(':')
                    print(book_info,book_info[0],book_info[1])
                    book[book_info[0]] = book_info[1]
                print(f"book:{book}")
                books.append(book)


if __name__ == '__main__':
    book_manager()

