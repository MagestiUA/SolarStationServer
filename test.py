import redis

client = redis.Redis(host='localhost', port=6379)
try:
    client.ping()
    print("Підключення до Redis встановлено!")
except redis.exceptions.ConnectionError:
    print("Не вдалося підключитися до Redis.")
