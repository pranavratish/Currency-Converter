import os
import sys
from time import sleep
import json
from simple_term_menu import TerminalMenu
from halo import Halo
from classes import User
from classes import Conversion as cn
from classes import CurrencyConverter as cc
from classes import BtcConversion as bc
from classes import Log

os.system('clear')

def start():
    MainMenuTitle = ' Currency Converter\n'
    MainMenuOptions = [
        'Login',
        'New User',
        'Exit'
    ]
    MainMenuCursor = '> '
    MainMenuCStyle = ('fg_cyan', 'bold')
    MainMenuTheme = ('bg_black', 'fg_yellow')
    MainMenuExit = False

    MainMenu = TerminalMenu(
        menu_entries = MainMenuOptions,
        title = MainMenuTitle,
        menu_cursor = MainMenuCursor,
        menu_cursor_style = MainMenuCStyle,
        menu_highlight_style = MainMenuTheme,
        clear_screen = True
    )

    HomeMenuTitle = ' Home\n'
    HomeMenuOptions = [
        'Currency Conversion',
        'Bitcoin Conversion',
        'View Profile',
        'Exit to Main Menu'
    ]
    HomeMenuCursor = '> '
    HomeMenuCStyle = ('fg_cyan', 'bold')
    HomeMenuTheme = ('bg_black', 'fg_yellow')
    HomeMenuExit = False

    HomeMenu = TerminalMenu(
        menu_entries = HomeMenuOptions,
        title = HomeMenuTitle,
        menu_cursor = HomeMenuCursor,
        menu_cursor_style = HomeMenuCStyle,
        menu_highlight_style = HomeMenuTheme,
        clear_screen = True
    )

    ConvMenuTitle = ' Save to Fast Access Conversions?\n'
    ConvMenuOptions = [
        'Save',
        'Exit to Home'
    ]
    ConvMenuCursor = '> '
    ConvMenuCStyle = ('fg_cyan', 'bold')
    ConvMenuTheme = ('bg_black', 'fg_yellow')
    ConvMenuExit = False

    ConvMenu = TerminalMenu(
        menu_entries = ConvMenuOptions,
        title = ConvMenuTitle,
        menu_cursor = ConvMenuCursor,
        menu_cursor_style = ConvMenuCStyle,
        menu_highlight_style = ConvMenuTheme,
        clear_screen = True
    )

    ProfileMenuTitle = ' Profile\n'
    ProfileMenuOptions = [
        'View Conversion Log',
        'View Bitcoin Conversion Log',
        'View Fast Access Conversions',
        'Edit Username',
        'Edit Password',
        'Delete Account',
        'Return to Profile'
    ]
    ProfileMenuCursor = '> '
    ProfileMenuCStyle = ('fg_cyan', 'bold')
    ProfileMenuTheme = ('bg_black', 'fg_yellow')
    ProfileMenuExit = False

    Profile_menu = TerminalMenu(
        menu_entries = ProfileMenuOptions,
        title = ProfileMenuTitle,
        menu_cursor = ProfileMenuCursor,
        menu_cursor_style = ProfileMenuCStyle,
        menu_highlight_style = ProfileMenuTheme,
        clear_screen = True
    )

    QuickExit = False

    while not MainMenuExit:
        MainOps = MainMenu.show()

        if MainOps == 0:
            UserN = str(input('Please Enter Username:\n'))
            Pass = str(input('Please Enter Password:\n'))

            try:
                with open('./data/users.json', 'r') as r :
                    try:
                        Valid = json.load(r)
                    except json.JSONDecodeError:
                        Valid = {}
            except FileNotFoundError:
                Valid = {}            
            
            if UserN in Valid:
                if Pass in Valid[UserN]:
                    print(f'Welcome Back {UserN}')
                    spinner = Halo(text='Loading...', spinner='arc')
                    spinner.start()
                    sleep(3)
                    spinner.stop()
                    while not HomeMenuExit:
                        HomeOps = HomeMenu.show()

                        if HomeOps == 0:
                            while not QuickExit:

                                FromC = input('What currency will you be converting from (Only use ISO 4217 Currency Codes):\n')

                                ToC = input('What currency will you convert to (Only user ISO 4217 Currency Codes):\n')

                                try:
                                    Amount = float(input('How much will you convert:\n'))
                                except TypeError:
                                    print('Not an integer or decimal value.')
                                    QuickExit = True

                                userConv = cn(FromC, ToC, Amount, UserN, Pass)

                                try:
                                    print(userConv.convert())
                                    QuickExit = True
                                except TypeError:
                                    print('Error! Incorrect input.\nThe currencies must be written according to the ISO 4217 Currency Codes.')
                                    QuickExit = True

                                while not ConvMenuExit:

                                    ConvOps = ConvMenu.show()

                                    if ConvOps == 0:
                                        userFav = userConv.add_FAC()

                                        print(userFav)

                                        QuickExit = True
                                    
                                    elif ConvOps == 1:

                                        print('Returning to Home Menu...')

                                        QuickExit = True
                                QuickExit = False
                            QuickExit = False



                                