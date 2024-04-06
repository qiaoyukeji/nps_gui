import subprocess
import threading
import PySimpleGUI as sg

# 定义版本号和作者信息
version = "0.0.1"
author = "巧遇科技工作室"
about_me = "本程序是NPS内网穿透服务的GUI界面，用来辅助NPS内网穿透服务客户端进行使用，与之配套的NPS版本为0.26.10。"

def read_output(process, output_element):
    """
    读取子进程的输出并将其传递给GUI线程显示的函数
    """
    for line in process.stdout:
        output_element.print(line.strip())

    for line in process.stderr:
        output_element.print(line.strip())

# 定义GUI布局
layout = [
    [sg.Menu([['关于', ['本程序介绍','版本号', '作者']]])],
    [sg.Text("服务端地址(IP):"), sg.Input(default_text="nps.qiaoyukeji.cn",key="-ADDRESS-")],
    [sg.Text("服务端端口号:"), sg.Input(default_text="28024",key="-PORT-")],
    [sg.Text("验证密钥(vkey):"), sg.Input(key="-VKEY-")],
    [sg.Text("连接方式:"), sg.Input(default_text="tcp",key="-TYPE-")],
    [sg.Button("连接远程穿透服务器"), sg.Button("退出")],
    [sg.Output(size=(60, 10), key="-OUTPUT-")]
]

# 创建窗口
window = sg.Window("NPS内网穿透GUI工具（v0.0.1）", layout)
output_element = window["-OUTPUT-"]

# 事件循环
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "退出":
        break

    if event == "连接远程穿透服务器":
        address = values["-ADDRESS-"]
        port = values["-PORT-"]
        vkey = values["-VKEY-"]
        type = values["-TYPE-"]

        command = f"npc.exe -server={address}:{port} -vkey={vkey} -type={type}"
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        # 创建线程读取子进程输出并传递给GUI线程显示
        output_thread = threading.Thread(target=read_output, args=(process, output_element), daemon=True)
        output_thread.start()

    if event == "版本号":
        sg.popup(f"版本号: {version}")

    if event == "作者":
        sg.popup(f"作者: {author}")
    if event == "本程序介绍":
        sg.popup(f"{about_me}")

# 关闭窗口
window.close()