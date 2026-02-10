from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "nombre": "Raul David Yoque Sum",
        "cancion_favorita": "YAS"
    })

if __name__ == "__main__":
    app.run(debug=True)
