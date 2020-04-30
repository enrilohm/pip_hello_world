from pip_hello_world.get_data import get_path

def hello_world():
    with open(get_path('dummy.txt'),'r') as f:
        text=f.read()
    print(text)
