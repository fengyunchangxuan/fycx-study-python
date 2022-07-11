import sqlite3


class User:
    """用户类，用于操作sqlite3"""

    # 初始化
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.db = sqlite3.connect(self.db_path)
        self.cursor = self.db.cursor()
        print('Opened db successfully')

    def create(self):
        """创建用户表"""

        self.cursor.execute('''CREATE TABLE USER
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME           TEXT NOT NULL,
                AGE             INT NUT NULL,
                HEIGHT          INT,
                WEIGHT          INT);''')
        print('Table created successfully')

    def insert(self, name, age, height, weight):
        """插入一条用户数据"""

        self.cursor.execute("INSERT INTO USER (NAME,AGE,HEIGHT,WEIGHT) \
        VALUES ('%s',%d,%d,%d)" % (name, age, height, weight))
        print('Insert one record')

    def delete(self, id):
        """更新一条数据"""

        self.cursor.execute("DELETE from USER where id = %d" % id)
        print('Delete one record')

    def update(self, id, name='', age=0, height=0, weight=0):
        """更新一条数据"""

        # 四个属性都为空，直接返回
        if not name and age <= 0 and height <= 0 and weight <= 0:
            print('No record')
            return None

        execute = 'UPDATE USER set '

        if name:
            execute += "NAME = '%s'" % name

        if age > 0:
            execute += 'AGE = %d' % age

        if height > 0:
            execute += 'HEIGHT = %d' % height

        if weight > 0:
            execute += 'WEIGHT = %d' % weight

        execute += " where ID=%d" % (id)
        self.cursor.execute(execute)
        print('Update one record')

    def select(self):
        """查询数据"""

        rows = self.cursor.execute(
            'SELECT  id,name,age,height,weight FROM USER')
        return rows

    def close(self):
        """关闭db"""

        self.db.commit()
        self.db.close()


user = User('db/test')
# user.create()
user.insert('张三',8,110,45)
# user.insert('李四',18,120,55)
# user.insert('王五',28,130,65)
# user.insert('赵六',38,140,75)

rows = user.select()
for row in rows:
    print(row)

# user.update(1, '张二')
# user.update(1, '张三')
# user.delete(1)
rows = user.select()
for row in rows:
    print(row)
user.close()
