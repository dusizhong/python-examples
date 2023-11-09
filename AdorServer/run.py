from app import app

@app.route('/')
def home():
	return 'Hello, Ador Server!'

app.run(host='127.0.0.1', port=5000, debug=True)