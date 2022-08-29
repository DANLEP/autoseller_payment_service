from sqlalchemy import Table, Column, Integer, String, Float

from config.db import meta

subscriptions = Table(
    'subscription', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(45)),
    Column('days', Integer, unique=True),
    Column('price', Float),
)
