本程序使用 PySimpleGUI 为 NPS内网穿透客户端程序(v0.26.0)制作了一个GUI界面。


双击 dist 目录下的 NPS内网穿透客户端GUI程序.exe ，修改自己的配置文件，点击启动按钮即可。

或在本目录中自行编译，
```bash
pyinstaller --onefile --hidden-import PySimpleGUI main.py --name "NPS内网穿透客户端GUI程序"  --noconsole
```
然后将 npc.exe 文件复制到 dist 目录下即可。

nps/npc 版本为 0.26.0，可自行搜索下载。


![](http://img.upy.qiaoyukeji.cn/2024/04/06/20240406214012.png)