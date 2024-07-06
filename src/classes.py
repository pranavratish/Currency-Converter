from currency_converter import CurrencyConverter
from forex_python.bitcoin import BtcConverter
import json
import sys
import logging
from time import sleep
import pandas as pd
import requests as req
from api import API_KEY

# Set up logging module
logging.basicConfig(level=logging.INFO)

class User:

  def __init__(self, user, passw):
    self.user = user
    self.passw = passw
  
  def load_json(self, filepath):
    try:
      with open(filepath, 'r') as r:
        try:
          return json.load(r)
        except json.JSONDecodeError:
          return {}
    except FileNotFoundError:
      return {}
  
  def save_json(self, filepath, data):
    with open(filepath, 'w') as w:
      json.dump(data, w, indent=4)

  def create_user(self):

    Valid = self.load_json('./data/users.json')

    if self.user in Valid:
      return f'User {self.user} already exists. Please login to use Currency Converter.'
    else:
      Valid[self.user] = self.passw
      self.save_json('./data/users.json', Valid)

      UserStorage = self.load_json('./data/conversions.json')
      
      Entry = {
        f'{self.user}' : {}
      }

      UserStorage[len(UserStorage) + 1] = Entry

      self.save_json('./data/conversions.json', UserStorage)
      
      UserStorageB = self.load_json('./data/conversionsB.json')

      CounterB = len(UserStorageB)
      
      EntryB = {
        f'{self.user}' : {}
      }

      UserStorageB[CounterB + 1] = EntryB

      self.save_json('./data/conversionsB.json', UserStorageB)    
      
      UserStorageF = self.load_json('./data/fastaccessconv.json')

      CounterF = len(UserStorageF)
      
      EntryF = {
        f'{self.user}' : {}
      }

      UserStorageF[CounterF + 1] = EntryF

      self.save_json('./data/fastaccessconv.json', UserStorageF)

      return f'User {self.user} successfully created. Please login to use Currency Converter.'

  def update_user(self):

    Valid = self.load_json('./data/users.json')

    if self.user in Valid:
      NewUser = input('Please enter a new user name:\n')

      if NewUser in Valid:
        return f'user name {NewUser} already exists. Please choose a different username.'
      
      Valid[NewUser] = Valid.pop(self.user)

      self.save_json('./data/users.json', Valid)

      self.update_related(self.user, NewUser)

      self.user = NewUser

      return f'Username successfully update to {NewUser}'

    else:
      return 'Error: Unauthorized User in User Area! The application will now terminate...'
  
  def update_related(self, OldUser, NewName):

    Conv = self.load_json('./data/conversions.json')
    for key, entry in Conv.items():
      if OldUser in entry:
        entry[NewName] = entry[OldUser]
        del entry[OldUser]
    self.save_json('./data/conversions.json', Conv) 

    ConvB = self.load_json('./data/conversionsB.json')
    for key, entry in ConvB.items():
      if OldUser in entry:
        entry[NewName] = entry[OldUser]
        del entry[OldUser]
    self.save_json('./data/conversionsB.json', ConvB)

    ConvF = self.load_json('./data/fastaccessconv.json')
    for key, entry in ConvF.items():
      if OldUser in entry:
        entry[NewName] = entry[OldUser]
        del entry[OldUser]
    self.save_json('./data/fastaccessconv.json', ConvF)

  def update_passw(self):

    Valid = self.load_json('./data/users.json')
 
    if self.user in Valid:
      ConfirmPass = input('Please enter old password:\n')

      if ConfirmPass != self.passw:
        print('Incorrect password, returning to menu...')
        
      else:  
        NewPass = input('Please enter a new password:\n')
    
        Valid[self.user] = NewPass

        self.save_json('./data/users.json', Valid)

        print('password has been updated successfully')

    else:
      print('Error: Unauthorized User in User Area! The application will now terminate...')

  def delete_user(self):
    Valid = self.load_json('./data/users.json')
    ValidC = self.load_json('./data/conversions.json')
    ValidB = self.load_json('./data/conversionsB.json')
    ValidF = self.load_json('./data/fastaccessconv.json')
    
    if self.user in Valid:
      Confirm = input('Please re-enter your password to confirm deletion of account:\n')

      if Confirm == self.passw:
        print('Deleting Account...')
        for DataDict in (ValidC, ValidB, ValidF):
           for key, value in list(DataDict.items()):
              if self.user in value:
                del DataDict[key]
        
        self.save_json('./data/conversions.json', ValidC)
        
        self.save_json('./data/conversionsB.json', ValidB)
        
        self.save_json('./data/fastaccessconv.json', ValidF)
        
        del Valid[self.user]
        self.save_json('./data/users.json', Valid)

        print('Account deleted successfully, The application will close in 5 seconds...')
        sleep(5)
        sys.exit()
      else:
        return 'Invalid Password, returning to menu...'
  
class Log(User):
  def __init__(self, user, passw):
    super().__init__(user, passw)

  def display_conv(self, limit=None):

    LoggedC = self.load_json('./data/conversions.json')

    UsersLog = []
    for key, value in LoggedC.items():
        if self.user in value:
            UsersLog.extend(dict(value[self.user]).values())

    if not UsersLog:
        print(f"No conversion logs found for user {self.user}.")
        return

    DisplayDF = pd.DataFrame(UsersLog)

    if limit != None:
      DisplayDF = DisplayDF.tail(limit)

    print(DisplayDF)
  
  def display_convB(self, limit=None):

    LoggedBC = self.load_json('./data/conversionsB.json')

    UsersLogB = []
    for key, value in LoggedBC.items():
        if self.user in value:
            UsersLogB.extend(dict(value[self.user]).values())

    if not UsersLogB:
        print(f"No Bitcoin conversion logs found for user {self.user}.")
        return

    DisplayBDF = pd.DataFrame(UsersLogB)

    if limit != None:
      DisplayBDF = DisplayBDF.tail(limit)

    print(DisplayBDF)

  def FAC_table(self):

    Fav = self.load_json('./data/fastaccessconv.json')

    SavedConv = []
    for key, value in Fav.items():
        if self.user in value:
            SavedConv.extend(dict(value[self.user]).values())

    if not Fav:
        return f"No saved conversions found for user {self.user}."

    DisplayF = pd.DataFrame(SavedConv)

    print(DisplayF)

class Conversion(User):
  
  c = CurrencyConverter()

  def __init__(self, from_c, to_c, amt, user, passw):
    super().__init__(user, passw)
    self.from_c = from_c
    self.to_c = to_c
    self.amt = amt

  def convert(self):
    try:
      ConvAmt = self.c.convert(self.amt, self.from_c, self.to_c)
      Conv = self.load_json('./data/conversions.json')
      
      Entry = {
        "from_cur": self.from_c,
        "to_cur": self.to_c,
        "amount": self.amt,
        "conversion": float(f'{ConvAmt:.2f}')
      }

      for key, value in dict(Conv).items():
        if self.user in value:
          Conv[key][self.user][len(value[self.user]) + 1] = Entry

      self.save_json('./data/conversions.json', Conv)

      Result = f'{self.amt} {self.from_c} = {ConvAmt:.2f} {self.to_c}'
      print(Result)
    except Exception as e:
      Error = f'Error occurred during conversion: {e}'
      print(Error)

  def add_FAC(self):
    # adding the conversion to fast access conversion json file

    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{self.from_c}/{self.to_c}'

    Conf = input('Are you sure you want to add this conversion rate to your Fast Access Conversions(type Y to proceed, type anything else to exit):\n')

    AnswY = 'Yy'

    if Conf in AnswY:
      Fav = self.load_json('./data/fastaccessconv.json')
      Response = req.get(url)
      Rate = Response.json()

      Entry = {
        "from_cur": self.from_c,
        "to_cur": self.to_c,
        "conv_rate": Rate["conversion_rate"]
      }

      for key, value in dict(Fav).items():
        if self.user in value:
          Fav[key][self.user][len(value[self.user]) + 1] = Entry
      
      self.save_json('./data/fastaccessconv.json', Fav)
      
      return 'Conversion added to Fast Access Conversions.'
    else:
      return 'The conversion rate will not be saved.'

class BtcConversion(Conversion):

  b = BtcConverter()

  def __init__(self, from_c, amt, user, passw):
    super().__init__(from_c, 'BTC', amt, user, passw)
  
  def b_convert(self):
    try:
      print('Starting Conversion...')
      logging.info('Starting Conversion...')
      
      ConvAmtB = self.b.convert_to_btc(self.amt, self.from_c)
      
      print(f'Converted Amount = {ConvAmtB}')
      logging.info(f'Converted Amount = {ConvAmtB}')

      ConvB = self.load_json('./data/conversionsB.json')
      
      EntryB = {
        "from_cur": self.from_c,
        "amount": self.amt,
        "BtcConversion": float(f'{ConvAmtB:.2f}')
      }

      for key, value in dict(ConvB).items():
        if self.user in value:
          ConvB[key][self.user][len(value[self.user]) + 1] = EntryB

      self.save_json('./data/conversionsB.json', ConvB)

      Result =  f'{self.amt} {self.from_c} = BTC {ConvAmtB:.2f}'

      logging.info(f'Conversion Result: {Result}')

      print(Result)
      return Result
    except Exception as e:
      Error = f'Error occurred during conversion: {e}'
      print(Error)
      return Error