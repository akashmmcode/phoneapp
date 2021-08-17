import psycopg2
import flask
import json
from flask import jsonify
from flask import Flask, request, Response

con = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="akash"
)


def get_all(request):
    cur = con.cursor()
    cur.execute(
        "select sl_no,name from phonebook.phonebook order by sl_no ASC ")

    rows = cur.fetchall()

    return Response(
        json.dumps({
            "records": [{"sl_no": record[0], "name": record[1]} for record in rows]
        }),
        status=200,
        mimetype="application/json"
    )

    cur.close()

