# -*- coding: utf-8 -*-
import os

import pytest


if __name__ == '__main__':
    pytest.main(['-s','-v','-m p1','--alluredir=reports/temps', '--clean-alluredir'])

    os.system("allure generate reports/temps -o reports/allures --clean")

