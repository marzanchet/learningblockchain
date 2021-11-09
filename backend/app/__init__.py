from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)

@app.route('/')

def default():
    return 'Welcome to the blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain)

app.run(port=5001)