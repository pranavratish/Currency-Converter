from currency_converter import CurrencyConverter
from forex_python.bitcoin import BtcConverter
import json
import pandas as pd
import requests as req
from api import API_KEY

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

  def update_user(self):

    try:
      with open('./data/users.json', 'r') as r :
        try:
          Valid = json.load(r)
        except json.JSONDecodeError:
          Valid = {}  
    except FileNotFoundError:
      Valid = {}

    if self.user in Valid:
      NewUser = input('Please enter a new user name:\n')

      if NewUser in Valid:
        return f'user name {NewUser} already exists. Please choose a different username.'
      
      Valid[NewUser] = Valid[self.user]

      self.user = NewUser

      del Valid[self.user]

      with open('./data/users.json', 'w') as w :
        json.dump(Valid, w, indent=4)

      print(f'Username has been updated to {NewUser}')

    else:
      print('Error: Unauthorized User in User Area! The application will now terminate...')

  def update_passw(self):

    try:
      with open('./data/users.json', 'r') as r :
        try:
          Valid = json.load(r)
        except json.JSONDecodeError:
          Valid = {}  
    except FileNotFoundError:
      Valid = {}
 
    if self.user in Valid:
      ConfirmPass = input('Please enter old password:\n')

      if ConfirmPass != self.passw:
        print('Incorrect password, returning to menu...')
        
      else:  
        NewPass = input('Please enter a new password:\n')
    
        Valid[self.user] = NewPass

        with open('./data/users.json', 'w') as w :
          json.dump(Valid, w, indent=4)
        print('password has been updated successfully')

    else:
      print('Error: Unauthorized User in User Area! The application will now terminate...')

  def delete_user(self):

    try:
      with open('./data/users.json', 'r') as r :
        try:
          Valid = json.load(r)
        except json.JSONDecodeError:
          Valid = {}
    except FileNotFoundError:
      Valid = {}
    
    if self.user in Valid:
      Confirm = input('Please re-enter your password to confirm deletion of account:\n')

      if Confirm == self.passw:
        print('Deleting Account...')
        del Valid[self.user]        
        with open('./data/users.json', 'w') as w :
          json.dump(Valid, w)
        print('Account deleted successfully, returning to login...')
      else:
        print('Invalid Password, returning to menu...')
  
class Log(User):
  def __init__(self, user, passw):
    super().__init__(user, passw)

  def display_conv(self, limit=None):

    try:
        with open('./data/conversions.json', 'r') as r:
            LoggedC = dict(json.load(r))
    except FileNotFoundError:
        print("Conversion log file not found.")
        return
    except json.JSONDecodeError:
        print("Error reading the conversion log file.")
        return

    UsersLog = []
    for key, value in LoggedC.items():
        if self.user in value:
            UsersLog.extend(dict(value[self.user]).values())

    if not UsersLog:
        print(f"No conversion logs found for user {self.user}.")
        return

    DisplayDF = pd.DataFrame(UsersLog)

    if limit != None:
      DisplayDF = DisplayDF.head(limit)

    print(DisplayDF)
  
  def display_convB(self, limit=None):
    try:
        with open('./data/conversionsB.json', 'r') as r:
            LoggedBC = dict(json.load(r))
    except FileNotFoundError:
        print("Bitcoin Conversion log file not found.")
        return
    except json.JSONDecodeError:
        print("Error reading the Bitcoin conversion log file.")
        return

    UsersLogB = []
    for key, value in LoggedBC.items():
        if self.user in value:
            UsersLogB.extend(dict(value[self.user]).values())

    if not UsersLogB:
        print(f"No Bitcoin conversion logs found for user {self.user}.")
        return

    DisplayBDF = pd.DataFrame(UsersLogB)

    if limit != None:
      DisplayBDF = DisplayBDF.head(limit)

    print(DisplayBDF)

  def FAC_table(self):
    try:
        with open('./data/fastaccessconv.json', 'r') as r:
            Fav = dict(json.load(r))
    except FileNotFoundError:
        print("Fast Access Conversions file not found.")
        return
    except json.JSONDecodeError:
        print("Error reading the Fast Access Conversions file.")
        return

    SavedConv = []
    for key, value in Fav.items():
        if self.user in value:
            SavedConv.extend(dict(value[self.user]).values())

    if not Fav:
        print(f"No saved conversions found for user {self.user}.")
        return

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
    ConvAmt = self.c.convert(self.amt, self.from_c, self.to_c)
    # write conversion to json file after execution
    with open('./data/conversions.json', 'r') as r :
      Conv = json.load(r)
    
    Entry = {
      "from_cur": self.from_c,
      "to_cur": self.to_c,
      "amount": self.amt,
      "conversion": float(f'{ConvAmt:.2f}')
    }

    for key, value in dict(Conv).items():
      if self.user in value:
        Conv[key][self.user][len(value[self.user]) + 1] = Entry

    with open('./data/conversions.json', 'w') as w :
      json.dump(Conv, w, indent=4)

    # if this isnt working in the main file make sure you are printing the function
    return f'{self.amt} {self.from_c} = {ConvAmt:.2f} {self.to_c}'

  def add_FAC(self):
    # adding the conversion to fast access conversion json file

    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{self.from_c}/{self.to_c}'

    Conf = input('Are you sure you want to add this conversion rate to your Fast Access Conversions(type Y to proceed, type anything else to exit):\n')

    AnswY = 'Yy'

    if Conf in AnswY:
      try:
        with open('./data/fastaccessconv.json', 'r') as r:
          Fav = dict(json.load(r))
      except FileNotFoundError:
        print("Conversion log file not found.")
        return
      except json.JSONDecodeError:
        print("Error reading the conversion log file.")
        return
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
      
      with open('./data/fastaccessconv.json', 'w') as w :
        json.dump(Fav, w, indent=4)
      
      return 'Conversion added to Fast Access Conversions.'
    else:
      return 'The conversion rate will not be saved.'

class BtcConversion(Conversion):

  b = BtcConverter()

  def __init__(self, from_c, amt, user, passw):
    super().__init__(from_c, 'BTC', amt, user, passw)
  
  def b_convert(self):
    ConvAmtB = self.b.convert_to_btc(self.amt, self.from_c)

    with open('./data/conversionsB.json', 'r') as r :
      ConvB = json.load(r)
    
    EntryB = {
      "from_cur": self.from_c,
      "amount": self.amt,
      "BtcConversion": float(f'{ConvAmtB:.2f}')
    }

    for key, value in dict(ConvB).items():
      if self.user in value:
        ConvB[key][self.user][len(value[self.user]) + 1] = EntryB

    with open('./data/conversionsB.json', 'w') as w :
      json.dump(ConvB, w, indent=4)

    return f'{self.amt} {self.from_c} = BTC {ConvAmtB:.2f}'