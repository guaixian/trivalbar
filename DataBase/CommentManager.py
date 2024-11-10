from DataBase.SQLManagr import SqlManagr
class CommentManager(SqlManagr):
    def __init__(self,config_path):
        super().__init__(config_path)
        pass

    def create_table(self):
        """
        评论(UId):
        图片列表地址:
        文字描述:(who):(评论内容);(who):....
        时间:
        地点:
        点赞个数:

        :return:
        """
        # 创建Comments表的SQL语句
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Comments (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            spot_uid TEXT NOT NULL,  -- 关联景点的UID
                            user_id TEXT NOT NULL,   -- 评论者UID
                            image_urls TEXT,         -- 图片列表地址，使用;分隔
                            content TEXT,            -- 评论内容，格式为(who):(评论内容);(who):...
                            timestamp TEXT NOT NULL, -- 评论时间，格式可设为标准时间格式
                            location TEXT,           -- 评论地点
                            likes INTEGER DEFAULT 0  -- 点赞数，默认为0
                        )
                    ''')
        self.conn.commit()
        self.conn.close()

