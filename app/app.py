from flask import Flask, render_template, request
from model_utils import predecir_fraude

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        monto = float(request.form["amount"])
        hora = int(request.form["hour"])
        categoria = request.form["category"]
        ubicacion = request.form["location"]

        datos = {
            "amount": monto,
            "hour": hora,
            f"merchant_category_{categoria}": 1,
            f"location_{ubicacion}": 1
        }

        resultado = predecir_fraude(datos)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
