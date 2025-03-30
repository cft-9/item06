import pandas as pd
import numpy as np
from typing import Dict, List

class FeatureEngine:
    def __init__(self):
        self.features = {}
    
    def calculate_technical_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """计算技术指标"""
        try:
            # 计算移动平均线
            df['MA5'] = df['收盘'].rolling(window=5).mean()
            df['MA10'] = df['收盘'].rolling(window=10).mean()
            df['MA20'] = df['收盘'].rolling(window=20).mean()
            
            # 计算RSI
            delta = df['收盘'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            df['RSI'] = 100 - (100 / (1 + rs))
            
            # 计算MACD
            exp1 = df['收盘'].ewm(span=12, adjust=False).mean()
            exp2 = df['收盘'].ewm(span=26, adjust=False).mean()
            df['MACD'] = exp1 - exp2
            df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
            
            return df
        except Exception as e:
            print(f"计算技术指标失败: {e}")
            return df
    
    def calculate_fundamental_indicators(self, basic_info: Dict) -> Dict:
        """计算基本面指标"""
        try:
            indicators = {}
            # 这里可以根据basic_info中的数据进行基本面分析
            # 例如：市盈率、市净率、ROE等
            return indicators
        except Exception as e:
            print(f"计算基本面指标失败: {e}")
            return {} 