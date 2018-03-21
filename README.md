## 1. 使用一种ORM框架,将“数据1.csv” 入库到一个mysql数据库中
- 配置 models.py 文件中的数据库路径
- 运行 models.py 文件，即可将 csv 文件数据写入 mysql


## 2. 利用python从数据库表中提取该数据并分析该股票每周的成交额（turnover字段）均值，并用图形展示
- 运行 main.py 文件
- 用浏览器访问 "localhost:5000/stock",即可查看图表
