
from DataBase.SQLManagr import SqlManagr

class SpotManager(SqlManagr):
    def __init__(self,config_path):
        super().__init__(config_path)
        pass


    def create_table(self):
        """
        景点uid：
        所属省份(直辖市,湖北...）
        地区(重庆,三亚)
        景点名称：
        评分：
        地址：
        开放时间：
        官方电话：
        公告信息：
        󰺂热度：
        景点A级：  4A
        景点信息：
        景点图片列表：图片地址
        价格:


        :return:
        """

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Spot (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            uid TEXT UNIQUE NOT NULL,
                            province TEXT NOT NULL,
                            region TEXT NOT NULL,
                            name TEXT NOT NULL,
                            rating REAL CHECK(rating >= 0 AND rating <= 5),
                            address TEXT,
                            opening_hours TEXT,
                            official_phone TEXT,
                            announcement TEXT,
                            popularity INTEGER,
                            grade TEXT,
                            description TEXT,
                            image_urls TEXT,
                            price REAL
                        )
                    ''')
        self.conn.commit()
        self.conn.close()


    def SearchSpot(self, uid):
        pass