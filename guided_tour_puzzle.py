'''
Guided Tour Puzzle is a form of a proof of work algoritm to mine the blocks.
The number to be solved must be difficult to find but easy to verify.

'''

import hashlib
import json
import binascii
import os
from time import time
from uuid import uuid4
import random
import client



class GuidedTourPuzzle(object):

    def __init__(self, guide_number, shared_keys, secret_key, timestamp,client_addr):

        # (N>=2) the number of tour guides 
        self.guide_number = guide_number
        
        # The sequential order of the tour.
        self.guided_tour = []

        self.Ax = client_addr

        # Generated hash values 
        self.hashes=[]

        # Shared secret keys: 
        self.shared_keys= shared_keys
        
        #Secret key: K 
        self. secret_key = secret_key

        # Bir puzzle solving için kullanılacak timestamp
        self.timestamp = timestamp

        self.proof = 0

        self.last_pair = []

        self.first_server_request()
        self.puzzle_solving()
        self.result_pair()
        self.result_proof()


    # Initial puzzle generation 

    def first_server_request(self):
        self.hashes=[]
        h_zero= hashlib.sha256(str(str(self.Ax) + str(self.guide_number) + str(self.timestamp) + str(self.secret_key)).encode("utf-8"))
        self.hashes.append(h_zero)


    def guide_tour_order(self):

        ''' Rastgele belirlediğim toplam guide sayısı kadar guide üretecek. 
            Ürettiği guide ise sıralı bir şekilde guided_tour içinde duracak. 
            Örneğin N = 5 için rastgele üretilen guide_x'ler : G1 , G4, G1 , G10, G0
            Bunlar üretildiği sıra ile guide_tour dizisinde bekliyor. 
        
        '''
        for i in range(self.guide_number):
            guide_x = random.randint(1, 10)
            self.guided_tour.append(guide_x)
            i+=1
        return self.guided_tour



    def puzzle_solving(self):
        # önce tour order belirlenir.
        guided_tour= self.guide_tour_order()

        for i in range(1, self.guide_number):
            # Dizinin ilk elemanı o anki guide oluyor.
            guide_now= guided_tour[i]
            # Bir sonraki hashi hesaplarken hashes[0] değerini alacak. i dediğim değer de bulunduğu guide indexi
            next_hash= hashlib.sha256(str(str(self.hashes[i-1]) + str(i) + str(self.guide_number) + 
            str(self.Ax) + str(self.timestamp) + str(self.secret_key)).encode('utf-8'))
            self.hashes.append(next_hash)


    def result_pair(self):
        self.last_pair = [self.hashes[0], self.hashes[-1]]
        return self.last_pair
        

    def result_proof(self):
        self.proof =str(str(self.last_pair[0]) + str(self.last_pair[1]))

