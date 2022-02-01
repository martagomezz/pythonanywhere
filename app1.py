from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Mi aplicación desde github</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == '__main__':
	app.run()
