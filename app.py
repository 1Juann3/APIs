from flask import Flask, jsonify

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

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store_name(name):
    pass

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<sting:name>/item', method=['POST'])
def create_item(name):
    pass

@app.route('/store/<string:name>/item')
def get_store_items(name):
    pass

app.run(port = 5000)