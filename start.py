import os
import sys
import webbrowser
import time
import subprocess

def main():
    print("正在启动余氏股票分析系统...")
    print("=" * 50)
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 设置虚拟环境路径
    venv_python = os.path.join(current_dir, "venv", "Scripts", "python.exe")
    
    if not os.path.exists(venv_python):
        print("正在创建虚拟环境...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
        print("虚拟环境创建完成！")
    
    # 使用虚拟环境启动应用
    try:
        print("正在启动应用...")
        # 启动Streamlit应用
        process = subprocess.Popen([
            venv_python,
            "-m", "streamlit",
            "run", "app.py",
            "--server.address", "localhost",
            "--server.port", "8501",
            "--server.headless", "true"
        ])
        
        # 等待服务器启动
        time.sleep(3)
        
        # 自动打开浏览器
        webbrowser.open("http://localhost:8501")
        
        print("应用已启动！请在浏览器中查看。")
        print("=" * 50)
        print("按 Ctrl+C 可以停止应用")
        
        # 保持脚本运行
        process.wait()
        
    except KeyboardInterrupt:
        print("\n正在关闭应用...")
        process.terminate()
        print("应用已关闭！")
    except Exception as e:
        print(f"启动失败: {str(e)}")
        print("请确保已安装所有依赖包。")

if __name__ == "__main__":
    main() 