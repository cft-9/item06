import akshare as ak
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
        demo_daily = pd.DataFrame({
            '日期': dates,
            '开盘': np.random.normal(100, 5, len(dates)),
            '收盘': np.random.normal(100, 5, len(dates)),
            '最高': np.random.normal(105, 5, len(dates)),
            '最低': np.random.normal(95, 5, len(dates)),
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
            '流通市值': '2500亿'
        }
        
        return {
            'stock_list': stock_list,
            'daily_data': demo_daily,
            'basic_info': demo_basic
        }
    
    def get_stock_list(self) -> pd.DataFrame:
        """获取A股股票列表"""
        try:
            stock_info = ak.stock_info_a_code_name()
            return stock_info
        except Exception as e:
            print(f"获取股票列表失败，使用演示数据: {e}")
            return self.demo_data['stock_list']
    
    def get_stock_daily(self, stock_code: str, start_date: str, end_date: str) -> pd.DataFrame:
        """获取股票日线数据"""
        try:
            df = ak.stock_zh_a_hist(symbol=stock_code, start_date=start_date, end_date=end_date)
            return df
        except Exception as e:
            print(f"获取股票日线数据失败，使用演示数据: {e}")
            # 修改演示数据的日期范围
            demo_data = self.demo_data['daily_data'].copy()
            demo_data['日期'] = pd.date_range(start=start_date, end=end_date, freq='D')
            return demo_data
    
    def get_stock_basic_info(self, stock_code: str) -> Dict:
        """获取股票基本信息"""
        try:
            info = ak.stock_individual_info_em(symbol=stock_code)
            return info.to_dict()
        except Exception as e:
            print(f"获取股票基本信息失败，使用演示数据: {e}")
            return self.demo_data['basic_info'] 