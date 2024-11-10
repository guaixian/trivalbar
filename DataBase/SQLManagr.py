import sqlite3

import yaml


class SqlManagr():

    def __init__(self,config_path):
        self.config=self.read_config(config_path)
        self.db_name = self.config["localdatabase"]["name"]
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()


    def read_config(self,config_path : str="config.yml"):
        # 读取 YAML 文件
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        # 输出读取的内容
        return config

    def create_table(self):
        pass

