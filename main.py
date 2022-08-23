import uvicorn
from fastapi import FastAPI
from starlette.requests import Request

from routes.index import payment_method

app = FastAPI()

app.include_router(payment_method, prefix="/payment_method",)


@app.get('/subscription_type')
def subscription_type():
    return [
        {
            'id': 0,
            'name': '1 month',
            'days': 30,
            'price': 8.99
        },
        {
            'id': 1,
            'name': '3 month',
            'days': 90,
            'price': 19.99
        },
        {
            'id': 2,
            'name': '12 month',
            'days': 360,
            'price': 59.99
        }
    ]


@app.post('/create_invoice')
async def create_invoice(request: Request):
    body = await request.json()

    return {

    }


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
