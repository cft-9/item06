import pandas as pd
from typing import Dict, List
from data_source import DataSource
from feature_engine import FeatureEngine

class StockAnalyzer:
    def __init__(self):
        self.data_source = DataSource()
        self.feature_engine = FeatureEngine()
    
    def analyze_stock(self, stock_code: str, start_date: str, end_date: str) -> Dict:
        """分析单个股票"""
        try:
            # 获取数据
            daily_data = self.data_source.get_stock_daily(stock_code, start_date, end_date)
            basic_info = self.data_source.get_stock_basic_info(stock_code)
            
            # 计算指标
            daily_data = self.feature_engine.calculate_technical_indicators(daily_data)
            fundamental_indicators = self.feature_engine.calculate_fundamental_indicators(basic_info)
            
            # 生成分析结果
            analysis_result = {
                'stock_code': stock_code,
                'technical_analysis': self._analyze_technical(daily_data),
                'fundamental_analysis': fundamental_indicators,
                'recommendation': self._generate_recommendation(daily_data, fundamental_indicators)
            }
            
            return analysis_result
        except Exception as e:
            print(f"分析股票失败: {e}")
            return {}
    
    def _analyze_technical(self, df: pd.DataFrame) -> Dict:
        """技术分析"""
        try:
            analysis = {
                'trend': self._analyze_trend(df),
                'momentum': self._analyze_momentum(df),
                'volatility': self._analyze_volatility(df)
            }
            return analysis
        except Exception as e:
            print(f"技术分析失败: {e}")
            return {}
    
    def _analyze_trend(self, df: pd.DataFrame) -> str:
        """分析趋势"""
        if df['MA5'].iloc[-1] > df['MA20'].iloc[-1]:
            return "上升趋势"
        elif df['MA5'].iloc[-1] < df['MA20'].iloc[-1]:
            return "下降趋势"
        else:
            return "震荡趋势"
    
    def _analyze_momentum(self, df: pd.DataFrame) -> str:
        """分析动量"""
        if df['RSI'].iloc[-1] > 70:
            return "超买"
        elif df['RSI'].iloc[-1] < 30:
            return "超卖"
        else:
            return "中性"
    
    def _analyze_volatility(self, df: pd.DataFrame) -> str:
        """分析波动性"""
        volatility = df['收盘'].pct_change().std()
        if volatility > 0.02:
            return "高波动"
        elif volatility > 0.01:
            return "中等波动"
        else:
            return "低波动"
    
    def _generate_recommendation(self, df: pd.DataFrame, fundamental: Dict) -> str:
        """生成投资建议"""
        trend = self._analyze_trend(df)
        momentum = self._analyze_momentum(df)
        
        if trend == "上升趋势" and momentum == "超买":
            return "建议观望"
        elif trend == "下降趋势" and momentum == "超卖":
            return "可以考虑买入"
        elif trend == "上升趋势" and momentum == "中性":
            return "可以考虑持有"
        else:
            return "建议观望" 