import os
import sys
from time import sleep
import json
from simple_term_menu import TerminalMenu

os.system('clear')

def start():
    main_menu_title = ' Currency Converter\n'
    main_menu_options = [
        'Login',
        'New User',
        'Exit'
    ]
    main_menu_cursor = '> '
    main_menu_c_style = ('fg_cyan', 'bold')
    main_menu_theme = ('bg_black', 'fg_yellow')
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries = main_menu_options,
        title = main_menu_title,
        menu_cursor = main_menu_cursor,
        menu_cursor_style = main_menu_c_style,
        menu_highlight_style = main_menu_theme,
        clear_screen = True
    )

    home_menu_title = ' Home\n'
    home_menu_options = [
        'Currency Conversion',
        'Bitcoin Conversion',
        'View Profile',
        'Exit to Main Menu'
    ]
    home_menu_cursor = '> '
    home_menu_c_style = ('fg_cyan', 'bold')
    home_menu_theme = ('bg_black', 'fg_yellow')
    home_menu_exit = False

    home_menu = TerminalMenu(
        menu_entries = home_menu_options,
        title = home_menu_title,
        menu_cursor = home_menu_cursor,
        menu_cursor_style = home_menu_c_style,
        menu_highlight_style = home_menu_theme,
        clear_screen = True
    )

    conv_menu_title = ' Save to Fast Access Conversions?\n'
    conv_menu_options = [
        'Edit',
        'Delete',
        'Exit to Profile'
    ]
    conv_menu_cursor = '> '
    conv_menu_c_style = ('fg_cyan', 'bold')
    conv_menu_theme = ('bg_black', 'fg_yellow')
    conv_menu_exit = False

    conv_menu = TerminalMenu(
        menu_entries = conv_menu_options,
        title = conv_menu_title,
        menu_cursor = conv_menu_cursor,
        menu_cursor_style = conv_menu_c_style,
        menu_highlight_style = conv_menu_theme,
        clear_screen = True
    )

    Profile_menu_title = ' Profile\n'
    Profile_menu_options = [
        'View Conversion Log',
        'View Bitcoin Conversion Log',
        'View Fast Access Conversions',
        'Edit Username',
        'Edit Password',
        'Delete Account',
        'Return to Profile'
    ]
    Profile_menu_cursor = '> '
    Profile_menu_c_style = ('fg_cyan', 'bold')
    Profile_menu_theme = ('bg_black', 'fg_yellow')
    Profile_menu_exit = False

    eProfile_menu = TerminalMenu(
        menu_entries = Profile_menu_options,
        title = Profile_menu_title,
        menu_cursor = Profile_menu_cursor,
        menu_cursor_style = Profile_menu_c_style,
        menu_highlight_style = Profile_menu_theme,
        clear_screen = True
    )

