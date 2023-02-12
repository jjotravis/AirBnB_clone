#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from modelsl.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self):
        """
        Handles EOF to exit the program
        """
        print()
        exit()

    def help_EOF(self, arg):
        """
        Documentation for EOF
        """
        print("Exits the the program with formatting\n")

    def do_quit(self, command):
        """
        Exit the console
        """
        exit()

    def help_quit(self):
        """
        Documentation for EOF
        """
        print("Quit command to exit program\n")

    def emptyline(self):
        """
        Does nothing when input is empty and ENTER is pressed
        """
        pass

    def do_create(self, args):
        """
        Creates an instance of a class
        """
        if args:
            if args in globals():
                cls = globals()[args]
                new_obj = cls()
                new_obj.save()
                print(new_obj.id)
            else:
                print("**class doesn't exist**")
        else:
            print("**class name missing**")

    def help_create(self):
        """
        Documentation for create method
        """
        print("Creates instance of a class of any type available")
        print("[Usage]: create <className>\n")

    def do_show(self, arg):
        """
        Prints string representation of an instance based on class name and id
        """
        if arg:
            args = arg.split()
            try:   # check if class name exists
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("**instance id missing**")
                else:
                    name_id = args[0] + "." + args[1]
                    storage.reload()
                    file_data = storage.all()
                    for key, value in file_data.items():
                        if key == name_id:
                            print(value)
                        else:
                            print("**no instance found**")
                            return
            except KeyError:
                print("**class doesn't exist**")
        else:
            print("**class name missing")

    def help_show(self):
        """Documentation for show method"""
        print("Shows a class instance if it exists when given the id")
        print("[Usage]: show <className> <id>\n")

    def do_destroy(self, arg):
        """
        Deletes an instance of a class based on id and updates JSON file
        """
        if arg:
            args = arg.split()
            try:
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("**instance id missing**")
                else:
                    name_id = args[0] + "." + args[1]
                    storage.reload()
                    file_data = storage.all()
                    if name_id in file_data:
                        del file_data[name_id]
                        storage.save()
                    else:
                        print("**no instance found**")
            except KeyError:
                print("**class doesn't exist**")
        else:
            print("**class name missing**")

    def help_destroy(self):
        """Documentantion for delete method"""
        print("Deletes an instance of a classs based on id given")
        print("[Usage]: destroy <className> <id>")

    def do_update(self, arg):
        """
        Updates an instance of a class based on class and ID by adding or
        updating a given attribute
        """
        if arg:
            args = arg.split()
            if len(args) == 0:
                print("**class name missing**")
                return False
            if len(args) == 1:
                print("**instance id missing**")
                return False
            if len(args) == 2:
                print("**attribute name missing**")
                return False
            if len(args) == 3:
                print("**value missing**")
                return False

            class_name = args[0]
            id = args[1]
            attr_name = args[2]
            attr_value = args[3]

            if class_name not in globals():
                print("**Class does not exist**")
            else:
                name_id = class_name + "." + id
                storage.reload()
                reloaded = storage.all()
                for key, value in reloaded.items():
                    if key == name_id:
                        instance_dict = value
                        # Add attribute to dictionary
                        instance_dict[attr_name] = attr_value
                        # Add its value
                        storage.save()
                        break
                    else:
                        print("**Key not found**")

    def help_update(self):
        """
        Documentation for the update method
        """
        print("Updates an existing class instance\
            by adding a new attribute and its value")
        print("[Usage]: update <className> <id> 'Attr_name' 'Attr_value'")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
