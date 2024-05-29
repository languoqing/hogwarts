from homework_python.homework_20240526_pytest.Book import BookManagement


class Test_Book:

    def test_addBook(self):
        re = BookManagement().addBook('1', 'book1', 1, 'summary1')
        assert '添加成功' == re

    def test_modifyBookByID(self):
        re = BookManagement().modifyBookByID('1', 'book1', 1, 'summary1')
        assert '修改成功' == re

    def test_deleteBookByID(self):
        re = BookManagement().deleteBookByID('1')
        assert '删除成功' == re

    def test_deleteBookByName(self):
        re = BookManagement().deleteBookByName('book1')
        assert '删除成功' == re

    def test_queryBookByID(self):
        re = BookManagement().queryBookByID('1')
        assert '查询成功' == re

    def test_queryBookByID(self):
        re = BookManagement().queryBookByName('book1')
        assert '查询成功' == re

