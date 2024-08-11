from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1 style="color:blue;text-align:center;font-family:'Verdana',sans-serif;">Hello, World!</h1>
            <p style="font-size:20px;text-align:center;font-family:'Verdana',sans-serif;">Welcome to FastAPI</p>
        </body>
    </html>
    """