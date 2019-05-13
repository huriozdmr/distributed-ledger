from wtforms import Form, StringField, SelectField


class Tree ():
    def __init__(self):
        ''' Tree'yi oluşturmak için sınıflandırma: 
        OWASP TOP TEN
        A0 : Genesis
        A1 : Injection
        A2 : Broken Authentication
        A3 : Sensitive Data Exposure
        A4 : XML External Entities
        A5 : Broken Access Control
        A6 : Security Misconfiguration
        A7 : XSS
        A8 : Insecure Deserialization
        A9 : Using Components with Known Vulnerabilities
        A10: Insufficient Logging & Monitoring

        ''' 
        self.vul_tree = { "AO": [], "A1" : [] , "A2": [],   "A3": [] , 
                            "A4" : [],  "A5": [],   "A6": [],
                            "A7" : [] , "A8": [],   "A9": [] , 
                            "A10": []
                         }


    def searching_tree(self,Form):
        choices = self.vul_tree
        select = SelectField('Search for vulnerability:', choices=self.vul_tree)
        search = StringField('')
    

