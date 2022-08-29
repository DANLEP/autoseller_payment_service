from sqlalchemy import Table, Column, Integer, String

from config.db import meta

invoice_statuses = Table(
    'invoice_status', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(45), unique=True),
)
