from flask import render_template
from flask import Response
from flask import Blueprint
from models import StockData

import json
import time


# 创建蓝图
main = Blueprint('stock', __name__)


@main.route('/')
def index():
    return render_template('weekchart.html')


@main.route('/daychart')
def daychart():
    return render_template('daychart.html')


@main.route('/daydata')
def daydata():
    sd_list = StockData.query.all()
    # 遍历
    date = []
    turnover_list = []
    for s in sd_list:
        d = time.strftime("%Y/%m/%d", time.localtime(s.date))
        date.append(d)
        turnover_list.append(s.turnover)
    # 序列化，并发送
    text = []
    text.append(date)
    text.append(turnover_list)
    return Response(json.dumps(text), mimetype='application/json')


@main.route('/weekdata')
def weekdata():
    sd_list = StockData.query.all()
    date = []
    turnover_list = []
    # 遍历
    current_week = time.strftime("%Y%W", time.localtime(sd_list[0].date))
    day_counter = 0
    turnover_sum = 0
    for s in sd_list:
        d = time.strftime("%Y%W", time.localtime(s.date))
        if current_week == d:
            # 说明该日期在同一周
            # 累加交易额，累加天数
            turnover_sum += s.turnover
            day_counter += 1
        else:
            # 进入下一周了
            # 计算上一周的平均交易额，输出平均交易额和周
            perweek_turnover = turnover_sum / day_counter
            turnover_list.append(perweek_turnover)
            w = current_week[:4] + '年/第' + current_week[4:] + '周'
            date.append(w)
            # 修改 current_week 为当前周，重置 turnover_sum 和 day_counter
            current_week = d
            turnover_sum = s.turnover
            day_counter = 1
    # 将最后一周的数据输出
    perweek_turnover = turnover_sum / day_counter
    turnover_list.append(perweek_turnover)
    w = current_week[:4] + '年/第' + current_week[4:] + '周'
    date.append(w)
    # 序列化，并发送
    text = []
    text.append(date)
    text.append(turnover_list)
    return Response(json.dumps(text), mimetype='application/json')

