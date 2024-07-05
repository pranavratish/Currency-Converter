import os
import sys
from time import sleep
import json
from simple_term_menu import TerminalMenu
from halo import Halo

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
        'Edit',
        'Delete',
        'Exit to Profile'
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
        main_sel = MainMenu.show()

        if main_sel == 0:
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