from abc import ABC,abstractmethod

import json

class Book :
    def __init__(self,book_id, name, author,total_num):
        self.book_id = book_id      # 图书编号(公有属性)
        self.name = name            # 图书名称(公有属性)
        self.author = author        # 作者(公有属性)
        self.total_num = total_num  # 总数(公有属性)
        self.__available_num = total_num # 可用数量(私有属性)
    # 添加这个方法
    def __str__(self):
        return f"书号:{self.book_id}, 书名:《{self.name}》, 作者:{self.author}, 库存:{self.__available_num}"
    # 新增：为了在字典中也能显示具体内容，需要定义 __repr__
    def __repr__(self):
        return self.__str__()
    # 借阅图书
    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            print(f"成功借阅图书: {self.name}")
            return True
        else:
            print(f"图书: {self.name} 已被借完")
            return False

    # 归还图书
    def return_book(self):
        self.__available_num += 1
        print(f"成功归还图书: {self.name}")

    # 可用数量
    def get_available(self):
        return self.__available_num


# 抽象类: 抽象类不能实例化, 只能继承, 作用就是规定子类必须实现某些方法，强制子类必须遵循统计的代码规范
# Python中的抽象类: 需要继承abc模块中的ABC ABC(Abstract Base Class)
# 会员类
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id  # 会员编号(公有属性)
        self.name = name            # 姓名(公有属性)
        self.__password = password              # 密码(私有属性)
        self.borrowed_books = []           # 借阅图书列表(私有属性)
    # 借阅图书
    def borrow_book(self, book: Book):
        if len(self.borrowed_books) >= self.get_max_books():
            print("借阅失败，你借阅数量已达到最大限制！")
            return False
        # 判断书籍是否可借阅
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"会员: {self.name} 成功借阅图书: {book.name}")
            return True
        else:
            print(f"图书: {book.name} 已被借完")
            return False

    # 归还图书
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"会员: {self.name} 成功归还图书: {book.name}")
            return True
        else:
            print(f"归还失败, 你没有借阅图书: {book.name}")
            return False

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.borrowed_books

    # 最大借阅图书数量(抽象方法:需要在子类中实现)
    @abstractmethod
    def get_max_books(self) -> int:
        pass


# 普通会员类
class NormalMember(Member):
    def __init__(self, member_id, name, password):
        super().__init__(member_id, name, password)
    def __str__(self):
        return f"VIP会员:{self.name}(ID:{self.member_id})"
    # 新增：为了在字典中也能显示具体内容，需要定义 __repr__
    def __repr__(self):
        return self.__str__()
    def get_max_books(self) -> int:
        return 3


class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level
    # 输出会员信息
    def __str__(self):
        return f"VIP会员:{self.name}(ID:{self.member_id}), 会员等级:{self.vip_level}"
    # 新增：为了在字典中也能显示具体内容，需要定义 __repr__
    def __repr__(self):
        return self.__str__()
    def get_max_books(self) -> int:
        return 6 + self.vip_level


# 图书馆管理系统
class LibrarySystem:
    def __init__(self):
        self.books = {}  # 书籍列表 ---》{"AI001,Book对象}
        self.members = {} # 会员列表 ---》{"M001,Member对象}}
        self.current_member: Member|None = None #

        # 加载数据（书籍，会员)
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        # 加载书籍数据 data/books.json
        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                book_id = book["编号"]
                name = book["标题"]
                author = book["作者"]
                total_num = book["数量"]
                # book_id是键 Book对象是值
                self.books[book_id] = Book(book_id, name, author, total_num)
            print("加载数据数据成功")
    def load_members_data(self):
        # 加载会员数据 data/members.json
        with open("data/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                member_id = member["卡号"]
                name = member["姓名"]
                password = member["密码"]
                # member_id是键 Member对象是值
                if member_id.startswith("N"):
                    self.members[member_id] = NormalMember(member_id, name, password)
                elif member_id.startswith("V"):
                    self.members[member_id] = VIPMember(member_id, name, password, member["会员等级"])

            print("加载会员数据成功")

    def login(self):
        while True:
            print("【登录】")
            member_id = input("请输入会员卡号: ")
            password = input("请输入密码: ")

            member = self.members[member_id]
            # 判断会员卡号是否存在
            if member_id not in self.members:
                print("会员卡号不存在")
                continue
            if member.get_password() == password:
                self.current_member = member
                print(f"登录成功, 欢迎您: {member.name}")
                return True
            else:
                print("密码错误")
                continue

    def borrow_book(self):
        # 1.展示出当前图书馆的图书列表
        for book in self.books.values():
            print(book)
        # 2. 输入要借阅的图书编号
        book_id = input("请输入要借阅的图书编号: ")
        if book_id not in self.books:
            print("借阅失败，图书编号不存在")
            return
        self.current_member.borrow_book(self.books[book_id])

    def return_book(self):
        # 1. 展示出当前会员已借阅的图书列表
        for book in self.current_member.get_borrowed_books():
            print(f"编号{book.book_id},名称:{book.name}")
        # 2.获取用户输入的图书编号，执行还书操作
        book_id = input("请输入要归还的图书编号: ")
        if book_id not in self.books:
            print("还书失败，图书编号不存在")
            return
        self.current_member.return_book(self.books[book_id])

    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            for book in self.current_member.get_borrowed_books():
                print(f"编号{book.book_id},名称:{book.name}")
        else:
            print("没有已借阅图书")

    def run(self):
        if not self.login():
            print("登录失败")
            return
        while True:
            print("""
                1. 借阅图书
                2. 归还图书
                3. 查询已借阅图书
                4. 退出系统
            """)
            choice = input("请选择操作(1-4):")
            match choice:
                case "1":
                    self.borrow_book()
                case "2":
                    self.return_book()
                case "3":
                    self.show_borrowed_books()
                case "4":
                    print("Bye ~")
                    return
                case _:
                    print("非法操作")




if __name__ == '__main__':
    ls = LibrarySystem()
    # print(ls.books)
    # print(ls.members)
    ls.run()