from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from config.db import conn
from models.invoice_status import invoice_statuses
from schemas.invoice_status import InvoiceStatus


def get_invoice_statuses():
    return conn.execute(invoice_statuses.select()).fetchall()


def create_invoice_status(inv_st: InvoiceStatus):
    try:
        conn.execute(invoice_statuses.insert().values(
            name=inv_st.name
        ))
        return get_invoice_statuses()
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Invoice status duplicate (name)")


def invoice_status_on_startup():
    inv_st = get_invoice_statuses()
    if not inv_st:
        create_invoice_status(InvoiceStatus(name="Created"))
        create_invoice_status(InvoiceStatus(name="Paid"))
        create_invoice_status(InvoiceStatus(name="Canceled"))
