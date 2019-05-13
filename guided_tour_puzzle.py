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


    # Initial puzzle generation 

    def first_server_request(self, h_zero):


        h_zero= hashlib.sha256(self.Ax + self.guide_number + self.timestamp + self.secret_key)
        hashes.append(h_zero)

        return h_zero


    def guide_tour_order(guided_tour):

        ''' Rastgele belirlediğim toplam guide sayısı kadar guide üretecek. 
            Ürettiği guide ise sıralı bir şekilde guided_tour içinde duracak. 
            Örneğin N = 5 için rastgele üretilen guide_x'ler : G1 , G4, G1 , G10, G0
            Bunlar üretildiği sıra ile guide_tour dizisinde bekliyor. 
        
        '''
        for i in guide_number:
            guide_x = random.randint(1, 10)
            guided_tour.append(guide_x)
            i+=1
        return guided_tour



    def puzzle_solving(self):
        # önce tour order belirlenir.
        guided_tour= guide_tour_order()

        for i in range(1, guide_number):
            # Dizinin ilk elemanı o anki guide oluyor.
            guide_now= guided_tour[i]
            # Bir sonraki hashi hesaplarken hashes[0] değerini alacak. i dediğim değer de bulunduğu guide indexi
            next_hash= hashlib.sha256(hashes[i-1] + i + self.guide_number + 
            self.Ax + self.timestamp + self.secret_key)
            hashes.append(next_hash)


    def result_pair(self):
        length = len(self.hashes)
        self.last_pair = [self.hashes[0], self.hashes[length-1]]
        return last_pair
        

    def result_proof(self,proof):
        proof = last_pair[0] + last_pair [1]
        proof = self.proof
        return proof