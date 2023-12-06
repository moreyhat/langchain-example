# LangChain Caching
Caching response from Open AI API with Redis.

## Prerequisite
### Run Redis stack
```
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

### Install libraries
```
pip install -r requirements.txt
```

### Run the app
```
python app.py
```