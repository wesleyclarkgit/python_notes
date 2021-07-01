"""
Having fun learning abaout Blockchain tonight.  Going through this tutorial: https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

"""

# use JSON format to store data in each block

"""
{
    'author': 'author_name',
    'timestamp': 'transaaction_time',
    'data': 'transaction_data'

}
"""
# create a block class with above attributes.  make each block unique 
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

# how are hash values used in this context?  Adding has value to to-do list
from hashlib import sha256
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys = True)
        return sha256(block_string.encode()).hexdigest()


"""

Hashing each block ensures the security of each one individually, making it extremely difficult to tamper with the data within the blocks.  Now that we've established a single block let's put them together"""


"""
Blockchain code
Create a new class for the blockchain
To ensure immutability of entire blockchain, include a hash of the previous block within the current block.
The awareness of all data within each block establishes a mechanism for protecting the entire chain's integrity.  This is why we included previous_hash variable in the block class.   whaaaaaat!  defining the create_genesis_blockmethod creates an initial block of index 0 and a previous hash of 0.
"""

import time

class Blockchain:
    def __init__(self):
        self.unconfirmed_trasactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
        @property
        def last_block(self):
            return self.chain[-1] 


"""
Proof-Of-Work System
In order to implement a way for users to come to a consensus on a single chronological history the chain

POW system makes it progressively more difficult to perform the work required to make a new block.  Someone who modifies a previous block would have to redo the work of the block and all the blocks that follow it.  POW system requires scanning for a vlue with a certain number of zero bits when hashed.  The average work required to do this increases exponentially, therefore by increasing the difficulty with each new block, we can prevent users from modifying previous blocks

wow.  that's kinda unbelieveable
"""

difficulty = 2
def proof_of_work(self, block):
    block.nonce = 
    computed_hash = block.compute_hash()
    while not computed_has.startswith('0' * Blockchain.difficulty):
        block.nonce += 1
        computed_has = block.compute_hash()
    return computed_hash


"""
Add a few more methods to the blockchain class in order to put it together and construct a chain.  Initially, store the data of each transaction in unconfirmed_transactions.  Once the new block performs POW implement it into the chain.  This process of performing computational work within a system is known as mining.


"""

def add_block(self, block, proof):
    previous_hash = self.last_block.hash
    if previous_has != block.previous_hash:
        return False
    if not self.is_valid_proof(block, proof):
        return False
    block.hash = proof
    self.chain.append(block)
    return True

def is_valid_proof(self, block, block_hash):
    return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash ==block.compute_hash())

def add_new_transaction(self, transaction):
    return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())

def mine(self):
    if not self.unconfirmed_transactions:
        return False

    last_block = self.last_block

    new_block = Block(
        index=last_block.index + 1,
        transactions= self.unconfirmed_transactions,
        timestamp = time.time(),
        previous_hash = last_block.hash)

    proof = self.proof_of_work(new_block)
    self.add_block(new_block, proof)
    self.unconfirmed_transactions = []
    return new_block.index


    """
    Nice!  So far we:
    - defined a single block
    - defined a blockchain
    - defined a proof-of-work system
    - defined a mining procedure


    To use it, we build an interface which multiple users/nodes can interact.  Use Flash REST-API

    """

    from flask import Flask, request
    import requests

    app = Flask(__name__)

    blockchain = Blockchain()
    # define our web app and create a local blockchain.  Then, create an endpoint that allows us
    # to send a query to display relevant information on the blockchain

    @app.route('/chain', method=['GET'])
    def get_chain():
        chain_data = []
        for block in blockchain.chain:
            chain_data.append(block.__dict__)
        return json.dumps({"length": len(chain_data), "chain": chain_data})

    app.run(debug=True, port = 5000)

