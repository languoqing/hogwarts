import yaml
from yaml import Loader


class YamlUtil:

    file_path = ""
    @staticmethod
    def get_yaml_data(file_path=None):
        """获取yaml文件数据"""
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                data = yaml.load(f, Loader=Loader)
                return data
        except Exception as e:
            print(e)
            return None