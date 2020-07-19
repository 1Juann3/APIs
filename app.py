from flask import Flask, jsonify, request, render_template

app = Flask(__name__) 

stores = [
    {
        'name': 'store1',
        'items':[
            {
                'name': 'item1',
                'price': 10.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message': 'Store not found'})
    

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_items(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)

@app.route('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items'] })
    return jsonify({'message': 'Item not found'})

app.run(port = 5000)
