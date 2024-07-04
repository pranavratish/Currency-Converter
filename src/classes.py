import json
import os

class User:

  def __init__(self, user, passw):
    self.user = user
    self.passw = passw
  
  def create_user(self):

    try:
      with open('./data/users.json', 'r') as r :
        try:
          Valid = json.load(r)
        except json.JSONDecodeError:
          Valid = {}  
    except FileNotFoundError:
      Valid = {}

    if self.user in Valid:
      return f'User {self.user} already exists. Please login to use Currency Converter.'
    else:
      Valid[self.user] = self.passw
      with open('./data/users.json', 'w') as w :
        json.dump(Valid, w, indent=4)

      try:
        with open('./data/conversions.json', 'r') as r :
          try:
            UserStorage = json.load(r)
          except json.JSONDecodeError:
            UserStorage = {}
      except FileNotFoundError:
        UserStorage = {}
      
      Entry = {
        f'{self.user}' : {}
      }

      UserStorage[len(UserStorage) + 1] = Entry

      with open('./data/conversions.json', 'w') as w :
        json.dump(UserStorage, w, indent=4)
      
      try:
        with open('./data/conversionsB.json', 'r') as r :
          try:
            UserStorageB = json.load(r)
            CounterB = len(UserStorageB)
          except json.JSONDecodeError:
            UserStorageB = {}
      except FileNotFoundError:
        UserStorageB = {}
      
      EntryB = {
        f'{self.user}' : {}
      }

      UserStorageB[CounterB + 1] = EntryB

      with open('./data/conversionsB.json', 'w') as w :
        json.dump(UserStorageB, w, indent=4)     
      
      try:
        with open('./data/fastaccessconv.json', 'r') as r :
          try:
            UserStorageF = json.load(r)
            CounterF = len(UserStorageF)
          except json.JSONDecodeError:
            UserStorageF = {}
      except FileNotFoundError:
        UserStorageF = {}
      
      EntryF = {
        f'{self.user}' : {}
      }

      UserStorageF[CounterF + 1] = EntryF

      with open('./data/fastaccessconv.json', 'w') as w :
        json.dump(UserStorageF, w, indent=4) 

      return f'User {self.user} successfully created. Please login to use Currency Converter.'


