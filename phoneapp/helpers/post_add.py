import psycopg2
import flask
import json
from flask import Flask, request, Response

con = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="akash"
)


def post_add(request):

    data = request.json
    new_slno = data['sl_no']
    new_name = data['name']
    new_contact = data['contact_no']
    new_email = data['email']
    new_dob = data['dob']

    new_slno = int(new_slno)

    new_contact = int(new_contact)

    try:
        cur = con.cursor()
        cur.execute(
            f"insert into phonebook.phonebook(sl_no, name, contact_no, email, dob) values({new_slno}, '{new_name}', {new_contact}, '{new_email}', '{new_dob}');"
        )
        con.commit()

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

    return Response(status=200)


