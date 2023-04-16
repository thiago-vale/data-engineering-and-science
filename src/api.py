from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return '''
            <html>
                <head>
                    <title>MY FastApi</title>
                </head>
                    
                <body>
                    <div style="text-algin: center">
                        <h1> XP Educação </h1>
                    </div>
                </body>
            </html>
    
    '''


@app.get("/helthz")
async def root():
    return {
        "message":"ok!"
    } 