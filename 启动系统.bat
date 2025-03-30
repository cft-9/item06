@echo off
echo 正在启动余氏股票分析系统...
echo ================================================
echo 系统启动后会自动打开浏览器...
echo ================================================

cd /d "%~dp0"
.\venv\Scripts\python.exe -m streamlit run app.py --server.address localhost --server.port 8501

pause 