import random
from faker import Faker  
faker = Faker()  
import vulnerability
  
class Client():

    def __init__(self):
        
        self.client_addr= faker.ipv4()
        self.reputation_score= 0




    def get_reputation(self):
        return vulnerability.set_reputation()



    def view_profile(self,profile_info):
        profile_info = { 'Client address': self.client_addr,
                        'Reputation score':self.reputation_score}

        return profile_info