from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import time
import csv


app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 配置数据库的路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@host:3306/database'

db = SQLAlchemy(app)


class StockData(db.Model):
    __tablename__ = 'stock_data'
    id = db.Column(db.Integer, primary_key=True)
    wind_code = db.Column(db.String(20))
    name = db.Column(db.String(20))
    date = db.Column(db.Integer)
    time = db.Column(db.Integer)
    open_price = db.Column(db.Integer)
    highest_price = db.Column(db.Integer)
    lowest_price = db.Column(db.Integer)
    close_price = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    turnover = db.Column(db.Integer)
    pairing_item = db.Column(db.Integer)
    interest_rate = db.Column(db.Integer, default=0)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, row):
        self.wind_code = row[0]
        self.name = row[1]
        self.date = time.mktime(time.strptime(row[2], "%Y%m%d"))
        self.time = row[3]
        self.open_price = row[4]
        self.highest_price = row[5]
        self.lowest_price = row[6]
        self.close_price = row[7]
        self.volume = row[8]
        self.turnover = row[9]
        self.pairing_item = row[10]
        self.interest_rate = row[11]


if __name__ == '__main__':
    # 先 drop_all 删除所有数据库中的表
    # 再 create_all 创建所有的表
    db.drop_all()
    db.create_all()
    print('rebuild database')
    # 将 csv 文件数据存入数据库
    filename = '数据1.csv'
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        r = list(reader)
        for row in r[1:]:
            print(row)
            s = StockData(row)
            s.save()
