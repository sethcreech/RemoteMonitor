import json

from flask import Flask

from rmon_info import packAllInfo


app = Flask(__name__)

	
@app.route('/update')
def update():
	return json.dumps(packAllInfo())

	
if __name__ == "__main__":
	app.run(port=5001)