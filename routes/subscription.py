from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from config.db import conn
from models.subscriptions import subscriptions
from schemas.subscription import Subscription


subscription = APIRouter()


@subscription.get("/")
def get_subscriptions():
    return conn.execute(subscriptions.select().order_by(subscriptions.c.days)).fetchall()


@subscription.get("/{id}")
def get_subscription(id: int):
    sub = conn.execute(subscriptions.select().where(subscriptions.c.id == id)).fetchone()
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return sub


@subscription.post("/")
def create_subscription(tos: Subscription):
    try:
        conn.execute(subscriptions.insert().values(
            name=tos.name,
            days=tos.days,
            price=tos.price
        ))
        return get_subscriptions()
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Subscription duplicate (days)")


@subscription.put("/{id}")
def update_subscription(id: int, tos: Subscription):
    get_subscription(id)
    try:
        conn.execute(subscriptions.update().values(
            name=tos.name,
            days=tos.days,
            price=tos.price
        ).where(subscriptions.c.id == id))
        return get_subscription(id)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Subscription duplicate (days)")


@subscription.delete("/{id}")
def delete_subscription(id: int):
    get_subscription(id)
    conn.execute(subscriptions.delete().where(subscriptions.c.id == id))
    return get_subscriptions()


def subscription_on_startup():
    subs = conn.execute(subscriptions.select()).fetchall()
    if not subs:
        create_subscription(Subscription(name="1 month", days=30, price=9.99))
        create_subscription(Subscription(name="3 month", days=90, price=24.99))
        create_subscription(Subscription(name="1 year", days=365, price=49.99))