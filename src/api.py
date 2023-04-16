from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from redis import Redis

app = FastAPI()
redis = Redis(host='redis', port=6370)

@app.get("/", response_class=HTMLResponse)
async def root():
    redis.incr("count")
    count = str(redis.get("count"), 'utf-8')
    return f'''
            <html>
                <head>
                    <title>MY FastApi</title>
                </head>
                    
                <body>
                    <div style="text-algin: center">
                        <h1> count: {count} </h1>
                    </div>
                </body>
            </html>
    
    '''


@app.get("/helthz")
async def root():
    return {
        "message":"ok!"
    } 