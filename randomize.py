import yaml

def random_sechedule():
    print(yaml.__version__)
    with open('.github/workflows/automate.yml', 'r') as f:
        fs = f.read().replace('\non:', '\n"on":')
        y = yaml.load(fs)
    print(y)

if __name__ == '__main__':
    random_sechedule()