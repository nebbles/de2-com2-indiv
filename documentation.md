# Program Documentation
> *Version 1*  
> Benedict Greenberg  
> Design Engineering MEng, Imperial College London  
> DE2 Computing 2  
> Database Individual Assignment   

## Contents
1. [Installation](#1-installation)
2. [Navigating the menus](#2-navigating-the-menus)
3. [Features](#3-features)
  + [Database](#database)
  + [Import data](#import-data)
  + [Export data](#export-data)
  + [Add entries](#add-entries)
  + [Remove entries](#remove-entries)
  + [Quitting](#quitting)
4. [Debug mode](#4-debug-mode)

## 1. Installation

To run the database program, open a terminal (command) window and navigate to the working directory of the program and this documentation file. Example: 
```bash
$ cd /Users/username/Downloads/BenedictGreenberg
```

To start the program, execute run.py in the terminal (command) window.
```bash
$ python run.py
```

To run in debug mode (debug page opens at startup):
```bash
$ python run.py debug
```

**NB. It is important that _terminaltables_ is installed. If you do not have this package you will be redirected at start up and the program will not continue. For installation of _terminaltables_ please visit the [documentation website](https://robpol86.github.io/terminaltables/install.html).**

## 2. Navigating the menus

For navigating all menus, follow the on-screen prompts. At any time (except the main menu) you can type `..` or `back` to return to the previous menu.  In any menu you can type `quit` to exit the program. This is the recommended way to exit the program. If necessary use **CTRl+C** to exit at any time (any changes will not be saved). **NB. Menu navigation is not case sensitive.**

On every menu, to select a menu option simply type the option number, option name, or the first letter of the option.
```bash
MAIN MENU
1. Database
2. Import
3. Export
4. Add new entries
5. Remove entries
   Quit
```
E.g. To access the import menu use any of the following: `2` / `i` / `import`

## 3. Features

### Database
### Import data
### Export data
### Add entries
### Remove entries
### Quitting

When quitting you will be prompted to confirm you want to quit. You have three options:

1. `n` **no** - do not quit, return to previous menu
2. `y` **yes** - quit the program, any changes will not be saved
3. `s` **save** - quit and save the program, all changes will overwrite '*default_data.csv*'.

It is recommended you use the export feature in the main menu to export your data into the desired file before quitting.

## 4. Debug mode

