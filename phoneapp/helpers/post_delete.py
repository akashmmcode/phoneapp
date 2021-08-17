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


def post_delete(request):
    data = request.json
    new_slno = data["sl_no"]
    new_slno = int(new_slno)

    try:
        cur = con.cursor()
        cur.execute(
            f"delete from phonebook.phonebook where sl_no = '{new_slno}' returning sl_no;"
        )

        res = cur.fetchall()

        print(res)
        print(len(res))

        con.commit()

        if len(res) == 0:
            raise InputParamError("Serial number not found")
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


