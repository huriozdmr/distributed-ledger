import hashlib, json, time, flask, requests, random, os, binascii
import guided_tour_puzzle, client, vulnerability, tree
from uuid import uuid4
from urllib.parse import urlparse
from flask import flash, render_template, request, redirect
from flask import Flask, jsonify
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

from flask_wtf.csrf import CSRFProtect


class TheLedger():
    def __init__(self):

        self.nodes = set()
        # Yeni eklenen vuln buraya gelir.
        self.current_submits = []

        # Consensus dan sonra valid icine atilir. Tek olcak
        self.valid_submit = []

        # Create the genesis block to seed our initial block
        self.create_new_block(previous_hash=1, proof=100)

        #self.timestamp = time()

    def create_new_block(self, proof, previous_hash=None):
        '''
        Creates a new block to add the legder

        proof: The proof of work value that is resulted from Guided Tour puzzle protocol. 
        previous_hash: The hash value of the previous block

        '''
        block = {
            'index':
            len(self.current_submits) + 1,
            'proof':
            proof,
            'previous_hash':
            previous_hash or self.hashing_block(self.current_submits[-1]),
        }

        self.current_submits.append(block)
        return block

    def new_submit(self, new_vuln):
        '''
        Creates new submission process to vulnerability tree from a client
        cli_addr: client address that will add a new vulnerability to tree
        block_id: block id number that will be added to tree

        '''

        new_vuln = vulnerability

        self.current_submits.append({
            "vuln_name": new_vuln.vuln_name,
            "type": new_vuln.vuln_type,
            "description": new_vuln.short_descr,
            "CVSS": new_vuln.CVSS,
            "platform": new_vuln.platform,
        })

        return self.last_block['index'] + 1

    # Returns the index of last block in the tree
    def last_block(self):
        return self.current_submits[-1]

    def hashing_block(block):
        '''
        Hashes the block with SHA 256 cryptographic algorithm.

        '''
        # Ensure that the dictionary of the created block is ordered to avoid inconsistent hashes
        ordered_block = json.dumps(block, sort_keys=True).encode()

        # Returnes a string object of double length, containing only hexadecimal digits
        return hashlib.sha256(ordered_block).hexdigest()

    def register_node(self, address):
        """
        Add a new node to the list of nodes
        for example : 'http://192.168.0.5:5000'
        """

        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)


##########################################################
##########################################################
# FLASK #
##########################################################
##########################################################

# Instantiate our Node
app = Flask(__name__, template_folder='Content')

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the objects
theLedger = TheLedger()
new_client = client.Client()
new_tree = tree.Tree()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = new_tree.searching_tree(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    for key, value in new_tree.vul_tree.items():
        for val in value:
            if search in val:
                results.append(val)

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)


@app.route('/mine', methods=['GET'])
def mine():
    last_block = theLedger.last_block()
    #last_proof = last_block['proof']
    cli_addr = new_client.client_addr
    shared_keys = []
    timestamp = time.time()
    guide_number = random.randint(1, 10)
    secret_key = binascii.hexlify(os.urandom(24))

    # Guide sayisi kadar shared keys olusturulur
    for i in range(guide_number):
        shrd_key = binascii.hexlify(os.urandom(24))
        shared_keys.append(shrd_key)
        i += 1

<<<<<<< HEAD
    server = guided_tour_puzzle.GuidedTourPuzzle(guide_number, shared_keys,
                                                 secret_key, timestamp,
                                                 cli_addr)
    miner = guided_tour_puzzle.GuidedTourPuzzle(guide_number, shared_keys,
                                                secret_key, timestamp,
                                                cli_addr)
    # validation(server,miner)

=======
    server = guided_tour_puzzle.GuidedTourPuzzle(guide_number,shared_keys,secret_key,timestamp,cli_addr)
    miner = guided_tour_puzzle.GuidedTourPuzzle(guide_number,shared_keys,secret_key,timestamp,cli_addr)
    validation(server,miner)

    if validation:
        pass

>>>>>>> bfd6c6fcd954aad4afa61392335a38f17686a827
    # Forge the new Block by adding it to the tree
    #previous_hash = theLedger.hashing_block(last_block)
    previous_hash = 9
    proof = miner.proof
    block = theLedger.create_new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


def validation(server, miner):
    server_lp = server.result_pair()
    miner_lp = miner.result_pair()

    if (server_lp[0] == miner_lp[0] & server_lp[1] == miner_lp[1]):
        True

    else:
        False


class SubmitForm(Form):
    name = TextField("Name Of Student",
                     [validators.Required("Please enter  your name.")])
    submit = SubmitField("Send")


@app.route('/new-submit', methods=['GET', 'POST'])
def new_submit():

    form = SubmitForm()

    if request.method == "POST":
        print("\n\n\n\n", form)

        # values = request.get_json()

        # required = ['vuln_name', 'type', 'description', 'CVSS', 'platform']
        # if not all(k in values for k in required):
        #     return 'Missing values', 400

        # # Create a new submit process
        # index = theLedger.new_submit(values['vuln_name'], values['type'],
        #                              values['description'], values['CVSS'],
        #                              values['platform'])

        message = "The new submit will be added to Tree" + index
        response = {'message': message}
        return jsonify(response), 201
    else:
        return render_template('submit-request.html', form=form)


@app.route('/vulnerability-tree', methods=['GET'])
def full_tree():

    # Dict formatinda bu sekilde calisir mi?
    response = {
        'tree': new_tree.vul_tree,
        'length': len(new_tree.vul_tree),
    }
    return jsonify(response), 200


@app.route('/vulnerability-detail', methods=['GET'])
<<<<<<< HEAD
@app.route('/profile', methods=['GET'])
def view_profile():
    return jsonify(new_client.view_profile()), 200
=======



>>>>>>> bfd6c6fcd954aad4afa61392335a38f17686a827


if __name__ == '__main__':

    app.run(debug=True)
