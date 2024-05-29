import pytest

from homework_python.homework_20240526_pytest.Book import BookManagement
from homework_python.homework_20240526_pytest.util import yaml_util

book_data = yaml_util.YamlUtil.get_yaml_data('case_add_book.yaml')
print(book_data)
class TestBooKAddTag:

    def setup_class(self):
        self.bm = BookManagement()

    @pytest.mark.smoke
    @pytest.mark.parametrize('bid, name, price, summary',book_data.get('books'))
    def test_addBook(self, bid, name, price, summary):
        re = self.bm.addBook(bid, name, price, summary)
        assert '添加成功' == re

    @pytest.mark.smoke
    def test_modifyBookByID(self):
        re = self.bm.modifyBookByID('book1', 'book1', 1, 'summary1')
        assert '修改成功' == re

    @pytest.mark.p1
    def test_queryBookByID(self):
        re = self.bm.queryBookByID('book1')
        assert '查询成功' == re

    @pytest.mark.p1
    def test_queryBookByName(self):
        re = self.bm.queryBookByName('name2')
        assert '查询成功' == re

    @pytest.mark.smoke
    def test_deleteBookByID(self):
        re = self.bm.deleteBookByID('book1')
        assert '删除成功' == re

    @pytest.mark.p1
    def test_deleteBookByName(self):
        re = self.bm.deleteBookByName('name1')
        assert '删除成功' == re

