本程序使用 PySimpleGUI 为 NPS内网穿透客户端程序(v0.26.0)制作了一个GUI界面。

pyinstaller --onefile --hidden-import PySimpleGUI main.py --name "NPS内网穿透客户端GUI程序"  --noconsole