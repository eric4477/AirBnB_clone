#!/usr/bin/python
"""
class HBNBCommand that inherits
from cmd.Cmd
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    """
    # adding custom prompt
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        This function returns True, 
        indicating a request to quit.
        """
        return True

    def help_quit(self):
        """
        This function prints a message indicating the 'Quit' 
        command's purpose, which is to exit the program.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        This function handles the end-of-file (EOF) signal, 
        typically triggered by typing 'EOF'. It prints a 
        newline character and returns True.
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
