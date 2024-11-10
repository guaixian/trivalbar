from DataBase.SQLManagr import SqlManagr


class UserManager(SqlManagr):
    def __init__(self, config_path):
        super().__init__(config_path)
        pass

    def createUser(self, username, password):
        pass

    def create_table(self):
        """
        UID:uuid.uuid().hex  string
        账号：使用邮箱注册QQ 类似邮箱  string
        密码: ASE加密得到的密码 string
        昵称: 任意名称不包含特殊字符 长度为10 一下 string
        头像: 图片地址（http，https) 或者 base64图片数据
        点赞: 景点id;景点id;  记录点赞的每个id 以; 分割
        收藏: 景点id;景点id;  记录点赞的每个id 以; 分割
        历史记录:景点id;景点id;  记录点赞的每个id 以; 分割
        评论: 景点id;景点id;  记录点赞的每个id 以; 分割
        :return:
        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    UID TEXT UNIQUE NOT NULL,
                    account TEXT NOT NULL,
                    password TEXT NOT NULL,
                    nickname TEXT CHECK(LENGTH(nickname) <= 10),
                    avatar TEXT,
                    likes TEXT,
                    favorites TEXT,
                    history TEXT,
                    comments TEXT
                )''')
        self.conn.commit()
        self.conn.close()


    def getUser(self, uid):
        pass
