from base64 import encode
from calendar import c
import datetime
from re import A
import hashlib


class Actor:

    def __init__(self, fName, sName, timestampCreate, recipient, ammount, privKey):
        self.fName = fName
        self.sName = sName
        self.timestampCreate = timestampCreate
        self.recipient = recipient
        self.ammount = ammount
        self.privKey = privKey

    def dataBundle(self):
        return f"{self.fName};{self.sName};{self.timestampCreate};{self.recipient};{self.ammount};"

    def hashDataBundle(self):
        return hashlib.sha256((self.dataBundle() + self.privKey).encode(encoding = 'utf-8')).hexdigest()



