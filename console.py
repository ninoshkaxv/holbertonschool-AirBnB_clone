#!/usr/bin/python3

import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
        
    def do_quit(self, arg):
        """Handles program exit"""
        self.close()
        return True

    def do_EOF(self, arg):
        """Handle EOF"""
        return True
    
    def emptyline(self):
        """Handles an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
