#!/usr/bin/python3
"""
class HBNBCommand that inherits
from cmd.Cmd
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    """
    valid_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
    #  adding custom prompt
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
        #  saving the args into a variable
        args = shlex.split(arg)
        #  checking if there is no args
        if len(args) == 0:
            print("** class name missing **")
        #  checking if the args is not in valid_classes
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        #  if the args is in valid_classes, create a
        #  new instance from the first arg and save it (to the JSON file)
        else:
            new_instance = eval(f"{(args[0])}()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        #  saving the args into a variable
        args = shlex.split(arg)
        #  checking if there is no args
        if len(args) == 0:
            print("** class name missing **")
        #  checking if the args is not in valid_classes
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        #  checking if the args is missing the id
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            #  fetch or get all the objects from storage
            objects = storage.all()
            #  getting the <classname> and <id> from the args
            key = "{}.{}".format(args[0], args[1])
            #  if the key is in objects print the string
            #  representation of the instance
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        usage: destroy <class_name> <id>
        """
        #  saving the args into a variable
        args = shlex.split(arg)
        #  checking if there is no args
        if len(args) == 0:
            print("** class name missing **")
        #  checking if the args is not in valid_classes
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        #  checking if the args is missing the id
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            # fetch or get all the objects from storage
            objects = storage.all()
            #  getting the <classname> and <id> from the args
            key = "{}.{}".format(args[0], args[1])
            #  if the key is found delete the object and save
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
        # fetch or get all the objects from storage
        objects = storage.all()
        #  saving the args into a variable
        args = shlex.split(arg)
        #  checking if there is no args
        if len(args) == 0:
            #  loop in the objects and print the string
            #  representation for eack key
            for key, value in objects.items():
                print(str(value))
        #  checking if the args is not in valid_classes
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        #  if the classname is in valid_classes loop in the
        #  objects and find the exact classname and print
        #  it's instance string representation
        else:
            for key, value in objects.items():
                if key.split('.')[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file).
        """
        #  saving the args into a variable
        args = shlex.split(arg)
        #  checking if there is no args
        if len(args) == 0:
            print("** class name missing **")
        #  checking if the args is not in valid_classes
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        #  checking if the args is missing the id
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            # fetch or get all the objects from storage
            objects = storage.all()
            #  getting the <classname> and <id> from the args
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
            #  check if there is no attribute name
            elif len(args) < 3:
                print("** attribute name missing **")
            #  check if there is no value for the attribute name
            elif len(args) < 4:
                print("** value missing **")
            #  if the attribute name and attribute value exist
            else:
                # get the object from objects
                obj = objects[key]
                # get the the name attribute from args
                attrib_name = args[2]
                # get the the value attribute from args
                attrib_value = args[3]
                # try using the eval to attrib_value
                try:
                    attrib_value = eval(attrib_value)
                except Exception:
                    pass
                # setting and saving the attributes to the
                # object
                setattr(obj, attrib_name, attrib_value)
                storage.save()

    def emptyline(self):
        """
        return nothing when an empty line is entered
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
