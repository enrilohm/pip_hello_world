from data import get_data_path

def hello_world():
    with open(get_data_path('dummy.txt'),'r') as f:
        text=f.read()
    print(text)
