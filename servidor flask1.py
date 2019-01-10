from flask import Flask
from dbconnect22 import get_tickets
from dbconnect22 import get_tickets22
from dbconnect22 import get_groups
import json

app = Flask(__name__)

@app.route("/updates")
def hello():
    tickets = get_tickets()
    json_tickets = json.dumps(tickets)
    return json_tickets


#en pruebas
@app.route("/updates22")
def two():
    tickets = get_tickets22()
    json_tickets = json.dumps(tickets)
    return json_tickets

@app.route("/groups")
def groups():
    groups = get_groups()
    json_groups = json.dumps(groups)
    return json_groups

if (__name__ == "__main__"):
	app.run(port = 5000)
