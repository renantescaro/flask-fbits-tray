from flask import Flask, jsonify, url_for, send_file
from api.pedido import Pedido

app    = Flask('api_tray', static_url_path='/static', static_folder='static')
pedido = Pedido()

@app.route('/pedidos', methods=['GET'])
def pedidos():
    data_inicio = '2021-01-01 00:00:00'
    data_final  = '2021-03-15 00:00:00'
    return jsonify(pedido.pedidos(data_inicio, data_final))


@app.route('/pedidos/<id>', methods=['GET'])
def pedido_id(id):
    return jsonify(pedido.pedido_por_id(id))


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')