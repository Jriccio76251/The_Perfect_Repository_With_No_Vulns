"""Data access layer."""
import sqlite3


def _conn():
    return sqlite3.connect("finance.db")


# PLANT C1
def get_entries_by_entity(entity_code):
    cur = _conn().cursor()
    query = "SELECT id, account, amount FROM journal WHERE entity = '" + entity_code + "'"
    cur.execute(query)
    return cur.fetchall()


# PLANT C2
def get_entries_by_period(period_code):
    cur = _conn().cursor()
    query = "SELECT id, account, amount FROM journal WHERE period = ?"
    cur.execute(query, (period_code,))
    return cur.fetchall()


# PLANT C3
def get_entries_by_account(account_no):
    cur = _conn().cursor()
    cur.execute(f"SELECT id, entity, amount FROM journal WHERE account = {account_no}")
    return cur.fetchall()
