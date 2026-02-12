from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "nombre": "Raul David Yoque Sum",
        "album_favorito": "Vamos a ver que pasa"
    })

if __name__ == "__main__":
    app.run(debug=True)
