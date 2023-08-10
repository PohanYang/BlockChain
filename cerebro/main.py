import backtrader as bt
class MyStrategy(bt.Strategy):
    def next(self):
        pass #策略核心部件

#初始化Cebro引擎
cerebro = bt.Cerebro()

# 给Cebro引擎添加策略
cerebro.addstrategy(MyStrategy)

# 给Cebro引擎添加数据
data = bt.feeds.YahooFinanceCSVData(dataname='TSLA.csv') 
cerebro.adddata(data) 

#运行Cebro引擎
cerebro.run()