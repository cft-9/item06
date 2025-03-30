import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta

class DataSource:
    def __init__(self):
        self.cache = {}
        self.demo_data = self._create_demo_data()
    
    def _create_demo_data(self) -> Dict:
        """创建演示数据"""
        # 创建示例股票列表
        stock_list = pd.DataFrame({
            'code': ['000001', '600000', '000858', '600036', '000333'],
            'name': ['平安银行', '浦发银行', '五粮液', '招商银行', '美的集团']
        })
        
        # 创建示例日线数据
        dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='D')
        base_price = 100
        prices = []
        current_price = base_price
        
        for _ in range(len(dates)):
            change = np.random.normal(0, 1)  # 随机涨跌
            current_price = current_price * (1 + change/100)  # 价格变动
            prices.append(current_price)
        
        prices = np.array(prices)
        demo_daily = pd.DataFrame({
            '日期': dates,
            '开盘': prices * (1 + np.random.normal(0, 0.005, len(dates))),
            '收盘': prices,
            '最高': prices * (1 + abs(np.random.normal(0, 0.01, len(dates)))),
            '最低': prices * (1 - abs(np.random.normal(0, 0.01, len(dates)))),
            '成交量': np.random.randint(1000000, 5000000, len(dates))
        })
        
        # 创建示例基本信息
        demo_basic = {
            '股票代码': '000001',
            '股票名称': '平安银行',
            '所属行业': '银行',
            '市盈率': '8.5',
            '市净率': '0.8',
            '总市值': '3000亿',
            '流通市值': '2500亿',
            '52周最高': '￥15.88',
            '52周最低': '￥9.88',
            '每股收益': '1.28',
            '股息率': '3.5%'
        }
        
        return {
            'stock_list': stock_list,
            'daily_data': demo_daily,
            'basic_info': demo_basic
        }
    
    def get_stock_list(self) -> pd.DataFrame:
        """获取A股股票列表"""
        return self.demo_data['stock_list']
    
    def get_stock_daily(self, stock_code: str, start_date: str, end_date: str) -> pd.DataFrame:
        """获取股票日线数据"""
        demo_data = self.demo_data['daily_data'].copy()
        mask = (demo_data['日期'].dt.strftime('%Y%m%d') >= start_date) & \
               (demo_data['日期'].dt.strftime('%Y%m%d') <= end_date)
        return demo_data[mask]
    
    def get_stock_basic_info(self, stock_code: str) -> Dict:
        """获取股票基本信息"""
        return self.demo_data['basic_info'] 