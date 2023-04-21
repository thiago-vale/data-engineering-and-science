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
        <meta charset="UTF-8"/>
        <head>
          <title>My FastApi</title>
        </head>

        <body style="background: radial-gradient(circle at 10% 20%, rgb(0, 0, 0) 0%, rgb(64, 64, 64) 90.2%);">
          <div style="text-align: center;line-height: 200px;color: rgb(255, 255, 0);">
            <h1>XP Educação | Aprenda com quem faz</h1>
            <p>{count}</p>
          </div>
          <div style="text-align: center;line-height: 200px;color: rgb(255, 255, 0);">
            <h1> Versão 2.0.0</h1>
          </div>
        </body>
      </html>  
  """
    
    '''


@app.get("/helthz")
async def root():
    return {
        "message":"ok!"
    } 