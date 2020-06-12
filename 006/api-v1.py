import flask
from flask import request, jsonify
import json
import sqlite3
import os

#data=json.load(open("batman_quotes.json") ,encoding="utf8")

#sqlite3 database.sqlite3< batman_sql.sql this command in cmd and sqlite folder in c

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<head><style>img{float:left;}h1{float:left;}@font-face {font-family: "batmo";src: url("C:/Users/Reddy/Desktop/ctf/batman_api/Bat.ttf");}body{font-family:batmo;}</style></head><body style="background-color:rgb(0,0,0);"><a href="/"><img class="avatar" src="https://i.pinimg.com/originals/26/86/8e/26868e6c76dda7049b530912919067df.jpg" alt="batman_logo" width="70" height="111"></a><h1 style="color:white;">Batman Archive</h1><br><br><br><br><br><br><br><br><br><br><br><br>
<p style="color:white;">A prototype API for quotes from dark knight trilogy.</p><br>
<p style="color:white;">move to api through this <a href='api' style="color:white;">link</a><embed src="odst.mp3" width="180" height="90" loop="false" autostart="true" hidden="true" />
</body>
'''

@app.errorhandler(404)
def page_not_found(e):
    return "<br><br><br><br><br><br><br><center><h1><big>404</big></h1><p>The resource could not be found.</p>", 404

@app.route('/api', methods=['GET'])
def api_all():
    conn = sqlite3.connect('C:\sqlite\database.sqlite3')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    data = cur.execute('SELECT * FROM batman;').fetchall()

    return jsonify(data)


@app.route('/api/quotes', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    issue = query_parameters.get('issue')
    quotee = query_parameters.get('quotee')

    query = "SELECT * FROM batman WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if issue:
        query += ' issue=? AND'
        to_filter.append(issue)
    if quotee:
        query += ' quotee=? AND'
        to_filter.append(quotee)
    if not (id or issue or quotee):
        return page_not_found(404)

    query = query[:-4] + ';'
    print(query)
    conn = sqlite3.connect('C:\sqlite\database.sqlite3')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


app.run()