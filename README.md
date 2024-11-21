# CampusTales

## 说明

- 我使用的python虚拟环境版本为3.12.4，我建议你们同样使用这个版本
- 根目录下有requirements.txt文件，可以据此安装所需依赖
- 依赖中包含了langchain、torch和pyside相关包，但不能保证安装完依赖一定就能跑；pyside还需额外配置相关路径（如果使用vscode的话）
- 参考的pyside教程：【【已完结】PySide6百炼成真，带你系统性入门Qt】 https://www.bilibili.com/video/BV1c84y1N7iL/?share_source=copy_web&vd_source=fa2f807e09c19899c64571cdc61e87e7



## 项目结构

### 根目录

- Game目录下为主要代码，下方详细介绍
- 在根目录下还有分词器m3e-base-huggingface，需要手动添加；如果这个分词器你没有请从[moka-ai/m3e-base · Hugging Face](https://huggingface.co/moka-ai/m3e-base)下载
- 其余为测试性内容

### Game

- *.ui 文件均为通过QtDesigner绘制的，可通过QtDesigner打开
- 这些ui文件可被编译为Ui_*.py文件以导入
- 带有test字样的均为测试用
- main.py为项目主逻辑，后续可能会重构/重命名后将里面的类分散到多个文件中方便管理
- Code_Ui.py负责管理ui和关联主逻辑，运行本文件以启动gui



## 一些可能有用的指令

```cmd
# 激活虚拟环境（在根目录下）：
.\venv\Scripts\activate

# 退出环境：
deactivate

# 列出安装的包：
pip list

# 一旦虚拟环境被激活，使用下面的命令来生成requirements.txt文件：
pip freeze > requirements.txt

# 尝试使用Pyinstaller打包为exe文件：
pyinstaller --name=CampusTales --icon=images/icon.ico --onefile --add-data "config.json:." --add-data "images:images" main.py

pyinstaller --name=CampusTales --onefile \
    --add-data "activity:activity" \
    --add-data "Agent:Agent" \
    --add-data "Animation:Animation" \
    --add-data "Event:Event" \
    --add-data "resource:resource" \
    --add-data "UI_resource:UI_resource" \
    --add-data "屏幕截图_2024-10-23_140034-removebg-preview.png:." \
    --add-data "conversation_history.db:." \
    --add-data "img黑夜1.png:." \
    --add-data "img黄昏1.png:." \
    --add-data "img落日1.png:." \
    --add-data "img清晨1.png:." \
    --add-data "README.md:." \
    cover_start.py

pyinstaller --name=CampusTales --onefile  --add-data "Game:Game" --add-data "conversation_history.db:." --add-data "README.md:." Game\cover_start.py

pyinstaller --name=CampusTales --onefile --console --add-data "Game:Game" --add-data "conversation_history.db:." --add-data "README.md:." Game\cover_start.py

pyinstaller --name=CampusTales --onefile --add-data "Game:Game" --add-data "conversation_history.db:." --add-data "README.md:." --hidden-import pydantic.deprecated.decorator Game\cover_start.py

```







