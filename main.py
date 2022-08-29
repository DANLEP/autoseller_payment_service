import uvicorn
from fastapi import FastAPI
from starlette.requests import Request

from routes.index import payment_method
from routes.invoice_status import invoice_status_on_startup
from routes.subscription import subscription, subscription_on_startup

app = FastAPI()

app.include_router(payment_method, prefix="/payment_method")
app.include_router(subscription, prefix="/subscription")


@app.post('/create_invoice')
async def create_invoice(request: Request):
    body = await request.json()

    return {

    }


@app.on_event("startup")
def startup_event():
    subscription_on_startup()
    invoice_status_on_startup()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
