from flask import Flask, request, json
from model.Registers import Registers
from model.Checkouts import Checkouts

app = Flask(__name__)

checkouts = Checkouts()
registers = Registers()

@app.route('/health', methods = ['GET'])
def health():
    return 'health', 200


@app.route('/add', methods=['POST'])
def add():
    data = request.form.to_dict()
    checkouts.add(cust_id=data['customer_id'], item_id=data['item_id'])
    registers.assign(cust_id=data['customer_id'])

    return json.dumps({'registers': registers.display(checkouts.items)}), 201


@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.form.to_dict()
    checkouts.remove(data['customer_id'])
    registers.remove(data['customer_id'])

    return json.dumps({'registers': registers.display(checkouts.items)}), 201


@app.route('/state', methods=['DELETE'])
def delete():
    checkouts.clear()
    registers.clear()

    return 'deleted', 200


if __name__ == '__main__':
    app.run(debug = True)
