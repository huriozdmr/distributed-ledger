import random
from faker import Faker  
from urllib.parse import urlparse


faker = Faker()  
class Client():

    def __init__(self):
        
        self.client_addr= faker.ipv4()
        self.reputation_score= 0
        self.nodes = set()

    
        def register_node(self, address):
            """
        Add a new node to the list of nodes
        for example : 'http://192.168.0.5:5000'
        """

        parsed_url = urlparse(self.client_addr)
        self.nodes.add(parsed_url.netloc)

    def get_reputation(self):
        self.reputation_score= vulnerability.set_reputation()
        


