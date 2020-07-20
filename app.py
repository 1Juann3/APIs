from flask import Flask, jsonify, request, render_template #import flask and some functions

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
def create_store():                        #create a store
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store_name(name):              #get the name of a store 
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message': 'Store not found'})
    

@app.route('/store')
def get_stores():                    #get the list of stores that has been created
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_items(name):                  
    request_data = request.get_json()       #create an item in the store that you want
    for store in stores:
        if store['name'] == name:
            new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)

@app.route('/store/<string:name>/item')
def get_items(name):                       #get an item with the name and the price 
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items'] })
    return jsonify({'message': 'Item not found'})

app.run(port = 5000)
