from sqlalchemy import Table, Column, Integer, String, SmallInteger
from config.db import meta

payment_methods = Table(
    'payment_method', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(45)),
    Column('network', String(45)),
    Column('address', String(45)),
    Column('currency', String(45)),
    Column('api_key', String(45)),
    Column('is_active', SmallInteger),
)