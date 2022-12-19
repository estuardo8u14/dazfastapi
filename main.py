from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    tiempo: str
    exchange: str
    ticker: str
    texto: str

@app.get("/")
async def root():
    return {"message": "Recivido Exitosamente"}

@app.post("/alerta")
async def alerta(request: Request):
    msg = request.json()
    tiempo = msg['time']
    exchange = msg['exchange']
    ticker = msg['ticker']
    texto = msg['texto']
    print(tiempo)
    print(exchange)
    print(ticker)
    print(texto)



    return await {
        'code': 'Exitosa',
        'msg': request.json()
    }
    