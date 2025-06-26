from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola papu, el backend ya funciona 🗿🔥'

if __name__ == '__main__':
    app.run(debug=True)
