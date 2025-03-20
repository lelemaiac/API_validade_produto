from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/validade/<quantidade>/<tipo>')
def validade(quantidade, tipo):
    """
    API para calcular validade de produtos

    ## Endpoint: /validade/<quantidade>/<tipo>

    ## Parâmetros:
    - quantidade: quantidade do produto
    - tipo: tipo do produto

    ## Resposta (JSON):
    ```json
    {
        "cadastrado_em":
        "quantidade":
        "tipo":
        "validade"
    }

    ## Erros possíveis (JSON):
    Se a rota estiver incorreta ou se o tipo estiver incorreto
    ```json
    """

    try:
        prazo = int(quantidade)
        meses = datetime.today() + relativedelta(months=prazo)
        anos = datetime.today() + relativedelta(years=prazo)
        semana = datetime.today() + relativedelta(weeks=prazo)
        dias = datetime.today() + relativedelta(days=prazo)

        validade = ""

        if tipo == "dias":
            validade = dias

        elif tipo == "meses":
            validade = meses

        elif tipo == "anos":
            validade = anos

        elif tipo == "semana":
            validade = semana

        else:
            print("Tipo invalido")

        return jsonify({
            "cadastrado_em": datetime.today().strftime('%d/%m/%Y'),
            "quantidade": int(prazo),
            "tipo": str(tipo),
            "validade": validade.strftime('%d/%m/%Y'),
        })

    except ValueError:
        return jsonify({
            "Rota inválida"
        })

if __name__ == '__main__':
    app.run(debug=True)
