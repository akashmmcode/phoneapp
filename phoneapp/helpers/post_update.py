import psycopg2
import flask
import json
from flask import Flask, request, Response
from .exceptions import InputParamError

con = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="akash"
)


def post_update(request):
    data = request.json
    new_slno = data["sl_no"]
    new_slno = int(new_slno)
    new_name = data["name"]
    new_contact = data["contact_no"]
    new_contact = int(new_contact)
    new_email = data["email"]
    new_dob = data["dob"]

    try:
        cur = con.cursor()
        cur.execute(
            f"UPDATE phonebook.phonebook SET name = '{new_name}',contact_no = {new_contact},email = '{new_email}',dob = '{new_dob}' WHERE sl_no = '{new_slno}' returning sl_no;"
        )

        row = cur.fetchall()
        print(row)
        print(len(row))
        con.commit()

        if len(row) == 0:
            raise InputParamError("sl_no not found to update")
        else:
            return Response(status=200)

    except Exception as _e:
        con.rollback()
        return Response(
            json.dumps({
                "error": str(_e)
            }),
            status=404
        )
    finally:
        cur.close()
