from models import app
from stock import main as stock_routes


# 注册蓝图
app.register_blueprint(stock_routes, url_prefix='/stock')


# 运行代码
# 默认端口是 5000
if __name__ == '__main__':
    app.run(debug=True)
