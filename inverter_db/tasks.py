from SolarStationServer.celery import app


@app.task(bind=True)
def hello_world_task(self, name):
    print(self)

    print(f'Hello, {name}!')
    return "OK"