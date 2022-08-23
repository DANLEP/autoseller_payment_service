from fastapi import APIRouter

from config.db import conn
from models.index import payment_methods
from schemas.payment_method import PaymentMethod

payment_method = APIRouter()


@payment_method.get("/")
def get_payment_methods():
    return conn.execute(payment_methods.select()).fetchall()


@payment_method.get("/{id}")
def get_payment_method(id: int):
    return conn.execute(payment_methods.select().where(payment_methods.c.id == id)).fetchone()


# @payment_method.post("/")
# def create_payment_method(pm: PaymentMethod):
#     conn.execute(payment_methods.insert().values(
#         name=pm.name,
#         network=pm.network,
#         address=pm.address,
#         currency=pm.currency,
#         api_key=pm.api_key,
#         is_active=pm.is_active
#     ))
#     return conn.execute(payment_methods.select()).fetchall()


@payment_method.put("/{id}")
def update_payment_method(id: int, pm: PaymentMethod):
    conn.execute(payment_methods.update().values(
        name=pm.name,
        network=pm.network,
        address=pm.address,
        currency=pm.currency,
        api_key=pm.api_key,
        is_active=pm.is_active
    ).where(payment_methods.c.id == id))
    return conn.execute(payment_methods.select().where(payment_methods.c.id == id)).fetchone()
