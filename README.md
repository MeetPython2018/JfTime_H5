# JfTime_H5

` 项目描述: 同步分享YouTube平台自媒体频道江峰时刻的音频节目，将其整理成音频和文字版，让更多的人能听见外面的声音。传播真相、刺穿谎言，给你不一样的时政评论。 `

#### 创建虚拟环境并进入

```python
#  python3.5以后venv创建/激活/退出虚拟环境
python3 -m venv .    #  创建虚拟环境
source bin/activate    #  激活虚拟环境
deactivate  #  退出虚拟环境

#  virtualenv用于创建独立的Python环境，多个Python相互独立，互不影响
pip install python-virtualenv
virtualenv myvenv  #  myvenv为虚拟环境名称，接下来所有模块都只会安装到该目录中去。
cd myvenv
source ./bin/activate

#  默认情况下，虚拟环境会依赖系统环境中的site packages，如果不想依赖这些package，那么可以加上参数 --no-site-packages建立虚拟环境：
virtualenv --no-site-packages [虚拟环境名称]
```

#### 虚拟环境中需要安装的python库

```python
pip install flask
pip install pymysql
```

