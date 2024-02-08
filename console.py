#!/usr/bin/python
"""
class HBNBCommand that inherits
from cmd.Cmd
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    """
    valid_classes = ["BaseModel"]
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
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        """
        # saving the commands into a variable
        commands = shlex.split(arg)
        # checking if there is no commands
        if len(commands) == 0:
            print("** class name missing **")
        # checking if the commands is not in valid_classes
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        # if the commands is in valid_classes, create a 
        # new instance and save it (to the JSON file)
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """
        # saving the commands into a variable
        commands = shlex.split(arg)
        # checking if there is no commands
        if len(commands) == 0:
            print("** class name missing **")
        # checking if the commands is not in valid_classes 
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        # checking if the commands is missing the id
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            # fetch or get all the objects from storage
            objects = storage.all()
            # getting the <classname> and <id> from the commands
            key = "{}.{}".format(commands[0], commands[1])
            # if the key is in objects print the string 
            # representation of the instance
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        usage: destroy <class_name> <id>
        """
        # saving the commands into a variable
        commands = shlex.split(arg)
        # checking if there is no commands
        if len(commands) == 0:
            print("** class name missing **")
        # checking if the commands is not in valid_classes 
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        # checking if the commands is missing the id
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            #fetch or get all the objects from storage
            objects = storage.all()
            # getting the <classname> and <id> from the commands
            key = "{}.{}".format(commands[0], commands[1])
            # if the key is found delete the object and save
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all 
        instances based or not on the class name
        """
        #fetch or get all the objects from storage
        objects = storage.all()
        # saving the commands into a variable
        commands = shlex.split(arg)
        # checking if there is no commands
        if len(commands) == 0:
        # loop in the objects and print the string
        # representation for eack key
            for key, value in objects.items():
                print(str(value))
        # checking if the commands is not in valid_classes 
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")  
        # if the classname is in valid_classes loop in the 
        # objects and find the exact classname and print 
        # it's instance string representation
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id 
        by adding or updating attribute (save the change into 
        the JSON file).
        """
        # saving the commands into a variable
        commands = shlex.split(arg)
        # checking if there is no commands
        if len(commands) == 0:
            print("** class name missing **")
        # checking if the commands is not in valid_classes 
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
         # checking if the commands is missing the id
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            #fetch or get all the objects from storage
            objects = storage.all()
            # getting the <classname> and <id> from the commands
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            # check if there is no attribute name
            elif len(commands) < 3:
                print("** attribute name missing **")
            # check if there is no value for the attribute name
            elif len(commands) < 4:
                print("** value missing **")
            # if the attribute name and attribute value exist
            else:
                #get the object from objects
                obj = objects[key]
                #get the the name attribute from commands
                attrib_name = commands[2]
                #get the the value attribute from commands
                attrib_value = commands[3]
                #try using the eval to attrib_value
                try:
                    attrib_value = eval(attrib_value)
                except Exception:
                    pass
                #setting and saving the attributes to the 
                #object
                setattr(obj, attrib_name, attrib_value)
                storage.save()   
                



    def emptyline(self):
        """
        return nothing when an empty line is entered
        """
        pass
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()
