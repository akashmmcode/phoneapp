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


def get_one(request):

    new_slno = request.args['sl_no']

    try:
        cur = con.cursor()
        cur.execute(
            f"select sl_no,name from phonebook.phonebook where sl_no = '{new_slno}';"
        )
        rows = cur.fetchall()
        print(rows)
        print(len(rows))

        con.commit()

        if len(rows) == 0:
            raise InputParamError("Serial number not found")
        else:
            return Response(json.dumps({
                "records": [{"sl_no": record[0], "name":record[1]} for record in rows]
            }),
                status=200,
                mimetype="application.json"
            )
# ___________________________________________________________________________________________-

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
