from uuid import uuid4

from flask import Flask

from sbc.blockchain import Blockchain

app = Flask(__name__)
# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


