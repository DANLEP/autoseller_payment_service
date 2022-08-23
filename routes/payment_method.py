from fastapi import APIRouter

from config.db import conn
from models.index import payment_methods
from schemas.payment_method import PaymentMethod

payment_method = APIRouter()


@payment_method.get("/")
def get_payment_methods():
    return conn.execute(payment_methods.select()).fetchall()
