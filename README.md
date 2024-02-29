![github-header-image(18)](https://github.com/ninoshkaxv/holbertonschool-AirBnB_clone/assets/143634181/ec0d1dd4-ea68-4d45-9477-fa5fdcc71b7d)

# 📝Description:

This is the first part of the Holberton project "AirBnB_clone". This project aims to create a command-line interpreter (CLI) for an AirBnB clone. HBnB is a simplified version of the popular lodging rental website AirBnB. The CLI allows users to interact with the AirBnB clone functionalities, such as managing objects (creating, updating, deleting), displaying information, and more.

# 📡Instalation

Clone this repository:
```
git clone
```

# 💻Command Interpreter:

The command interpreter is implemented using Python and provides both interactive and non-interactive modes.

## 🚀How to Start:

To start the command interpreter in interactive mode, run the following command:
```
shell

$ ./console.py
```

To start the command interpreter in non-interactive mode, pipe commands into the script using echo or cat:
```
shell

$ echo "help" | ./console.py
```

## ℹ️How to Use:

Once the command interpreter is running, you can use various commands to interact with the AirBnB clone functionalities. The available commands include help, quit, and more. Detailed descriptions of each command can be accessed using the help <topic> command.

## 🌟Examples:
```
Interactive Mode:

bash

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```
```
Non-Interactive Mode:

bash

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
#  📂Files and Directories:

    README.md: Description of the project and instructions on how to use the command interpreter.
    AUTHORS: List of all individuals contributing to the project.
    console.py: The main script for the command interpreter.
    models/: Implementation of the BaseModel class with common attributes and methods.
    tests/: Directory containing unit tests for all files, classes, and functions.
    
# 👥Contributors:

    [Ninoshka Perez & Koral Rivera]




