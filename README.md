# c-116

# installing virtualenv(virtual evironment) package

pip install virtualenv
Requirement already satisfied: virtualenv in c:\users\codin\appdata\local\programs\python\python38\lib\site-packages (20.14.1)
Requirement already satisfied: platformdirs<3,>=2 in c:\users\codin\appdata\local\programs\python\python38\lib\site-packages (from virtualenv) (2.5.1)
Requirement already satisfied: six<2,>=1.9.0 in c:\users\codin\appdata\local\programs\python\python38\lib\site-packages (from virtualenv) (1.16.0)
Requirement already satisfied: filelock<4,>=3.2 in c:\users\codin\appdata\local\programs\python\python38\lib\site-packages (from virtualenv) (3.6.0)
Requirement already satisfied: distlib<1,>=0.3.1 in c:\users\codin\appdata\local\programs\python\python38\lib\site-packages (from virtualenv) (0.3.4)

# checking the version of the package
virtualenv --version
virtualenv 20.14.1

# creating virtual environment
virtualenv sridatta
created virtual environment CPython3.8.6.final.0-64 in 1732ms
  creator CPython3Windows(dest=D:\Sridatta\whitehat_jr\c-116\sridatta, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\codin\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.0.4, setuptools==62.1.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

# activating virtual evironment
sridatta\scripts\activate

# installing flask
pip install flask
Collecting flask
  Downloading Flask-2.1.2-py3-none-any.whl (95 kB)
     ---------------------------------------- 95.2/95.2 KB 1.1 MB/s eta 0:00:00
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting click>=8.0
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ---------------------------------------- 96.6/96.6 KB 502.0 kB/s eta 0:00:00
Collecting Jinja2>=3.0
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ---------------------------------------- 133.1/133.1 KB 522.8 kB/s eta 0:00:00
Collecting Werkzeug>=2.0
  Downloading Werkzeug-2.1.2-py3-none-any.whl (224 kB)
     ---------------------------------------- 224.9/224.9 KB 457.8 kB/s eta 0:00:00
Collecting importlib-metadata>=3.6.0
  Downloading importlib_metadata-4.11.4-py3-none-any.whl (18 kB)
Collecting colorama
  Using cached colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting zipp>=0.5
  Using cached zipp-3.8.0-py3-none-any.whl (5.4 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.1-cp38-cp38-win_amd64.whl (17 kB)
Installing collected packages: zipp, Werkzeug, MarkupSafe, itsdangerous, colorama, Jinja2, importlib-metadata, click, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.1.2 click-8.1.3 colorama-0.4.4 flask-2.1.2 importlib-metadata-4.11.4 itsdangerous-2.1.2 zipp-3.8.0



# official documentation
https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/#:~:text=Creating%20Python%20Virtual%20Environment%20in%20Windows%20and%20Linux,Now%20if%20you%20are%20same%20directory%20then%20type%2C

