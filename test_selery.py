import requests


def test_celery():
    # responses = requests.get('https://sorar-station-monitor-3b53afc4534a.herokuapp.com/hello-world?name=Vitalii')
    responses = requests.get('http://127.0.0.1:8000/hello-world?name=Ivan')
    print(responses.status_code, responses.content)
    # requests.get('http://127.0.0.1:8000/hello-world?name=Ivan')
    # requests.get('http://127.0.0.1:8000/hello-world?name=Vlad')
    # requests.get('http://127.0.0.1:8000/hello-world?name=Oleg')
    # requests.get('http://127.0.0.1:8000/hello-world?name=Igor')
    # requests.get('http://127.0.0.1:8000/hello-world?name=Vladimir')
    # requests.get('http://127.0.0.1:8000/hello-world?name=Vasyl')
    # requests.get('http://127.0.0.1:8000/hello-world?name=Olena')


if __name__ == '__main__':
    test_celery()