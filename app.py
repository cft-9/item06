import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from stock_analyzer import StockAnalyzer
import requests
import time

def check_network():
    """检查网络连接状态"""
    try:
        requests.get("http://www.baidu.com", timeout=3)
        return True
    except:
        return False

def main():
    # 配置页面基本设置
    st.set_page_config(
        page_title="余氏股票分析系统",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # 添加CSS样式
    st.markdown("""
        <style>
        .main {
            padding: 20px;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # 检查网络状态
    is_online = check_network()
    if not is_online:
        st.warning("⚠️ 当前处于离线模式，使用演示数据进行展示")
    
    # 添加系统标题和说明
    st.title("余氏股票分析系统 📊")
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h3 style='color: #1f77b4;'>系统说明</h3>
        <p>本系统提供以下功能：</p>
        <ul>
            <li>股票技术分析</li>
            <li>基本面分析</li>
            <li>智能投资建议</li>
            <li>股票推荐（开发中）</li>
        </ul>
        <p style='color: #666; font-size: 0.9em;'>支持股票代码：000001（平安银行）、600000（浦发银行）、000858（五粮液）、600036（招商银行）、000333（美的集团）</p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        # 初始化分析器
        analyzer = StockAnalyzer()
        
        # 侧边栏
        st.sidebar.title("功能选择")
        page = st.sidebar.radio("选择功能", ["股票分析", "股票推荐"])
        
        if page == "股票分析":
            # 股票分析页面
            st.header("股票分析")
            
            # 创建两列布局
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # 输入股票代码
                stock_code = st.text_input("请输入股票代码（例如：000001）", help="输入6位股票代码")
            
            with col2:
                # 添加示例按钮
                if st.button("使用示例股票"):
                    stock_code = "000001"
                    st.write("已选择示例股票：平安银行(000001)")
            
            # 选择时间范围
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input("开始日期", datetime.now() - timedelta(days=365))
            with col2:
                end_date = st.date_input("结束日期", datetime.now())
            
            if st.button("开始分析", type="primary"):
                if stock_code:
                    with st.spinner("正在分析中..."):
                        # 模拟加载时间
                        time.sleep(1)
                        
                        # 获取分析结果
                        result = analyzer.analyze_stock(
                            stock_code,
                            start_date.strftime("%Y%m%d"),
                            end_date.strftime("%Y%m%d")
                        )
                        
                        if result:
                            # 显示分析结果
                            st.success("分析完成！")
                            
                            # 使用卡片式布局显示结果
                            col1, col2, col3 = st.columns(3)
                            
                            with col1:
                                st.info("趋势分析")
                                tech_analysis = result['technical_analysis']
                                st.write(f"📈 趋势：{tech_analysis['trend']}")
                                st.write(f"📊 动量：{tech_analysis['momentum']}")
                                st.write(f"📉 波动性：{tech_analysis['volatility']}")
                            
                            with col2:
                                st.info("投资建议")
                                st.write("🎯 " + result['recommendation'])
                            
                            with col3:
                                st.info("风险提示")
                                st.write("⚠️ 投资有风险，入市需谨慎")
                            
                            # 添加免责声明
                            st.markdown("""
                            <div style='background-color: #fff3cd; padding: 10px; border-radius: 5px; margin-top: 20px;'>
                                <p style='color: #856404; font-size: 0.9em;'>
                                    ⚠️ 免责声明：本系统提供的分析结果仅供参考，不构成投资建议。投资有风险，入市需谨慎。
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.error("分析失败，请检查股票代码是否正确")
                else:
                    st.warning("请输入股票代码")
        
        elif page == "股票推荐":
            # 股票推荐页面
            st.header("股票推荐")
            st.info("🚧 该功能正在开发中，敬请期待...")
            
        # 添加页脚
        st.markdown("""
        <div style='text-align: center; padding: 20px; margin-top: 50px; border-top: 1px solid #eee;'>
            <p style='color: #666;'>© 2024 余氏股票分析系统 | 专业、智能、可靠的股票分析工具</p>
        </div>
        """, unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"系统出现错误: {str(e)}")
        st.info("请刷新页面重试")

if __name__ == "__main__":
    main() 