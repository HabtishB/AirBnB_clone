

#!/usr/bin/python3
""" Module containing the HBNBC command lists """

import cmd
from models.base_model import BaseModel
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    """ A console class for AirBnB """

    prompt = '(hbnb)'
    
    def quit(self, arg):
        "Exists the program"
        return True

    def create(self, arg):
        """Usage: creates <class>
        creates a new class and prints its id
        """
        arg1 = parse(arg):
        if len(arg1) == 0:
            print("**class name missing**")
        elif arg1[0] not in HBNBCommand.__classes__:
            print("** class doesn't exist **")

    def show(self, arg):
        """Shows the string representation of an instance based on class
           name and instance id: <class>.id or <class>.show(<object.id>)
        """
        arg1 = parse(arg)
        obj_dict = storage.all()

        if len(arg1) == 0:
            print ("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes__:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg1[0], arg1[1])])

    def destroy(self, arg):
        """ Destroys an instance of a class based on id """
        arg1 = parse(arg):
        obj_dict = storage.all()
        if len(arg1) == 0:
            print ("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes__:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg1[0], arg1[1])]
            storage.save()

    def all(self, arg):
        """ prints all string representation of all instances, not or based 
            on class. eg $all BaseModel or $all """
        arg1 = parse(arg):
        if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes__:
            print("** class doesn't exist **")
        else:
            instance = []
            for obj in storage.all().values():
                if len(arg1) > 0 and arg1[0] == obj.__class__.__name__:
                    instance.append(obj.__str__())
                elif len(arg1) == 0:
                    instance.append(obj.__str__())
            print(instance)

    def update(self, arg):
        """updates a class instance of a given id by adding or
        updating a given attribute key/value pair or dictionary
        """
        arg1 = parse(arg)
        obj_dict = storage.all()

        if len(arg1) == 0:
            print("""** class name missing **""")
            return False
        if arg1[0] not in HNBNcomand.__classess:
            print("""** class doesn't exist **""")
            return False
        if len(arg1) == 1:
            print("""** instance id missing **""")
            return False
        if "{}.{}".format(arg1[0], arg1[1]) not in obj_dict.key():
            print("** attribute name missing **")
            return False
        if len(arg1) == 3:
            try:
                type(eval(arg1[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg1) == 4:
            obj = obj_dict["{}.{}".format(arg1[0], arg1[1])]
            if arg1[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg1[2]])
                obj.__dict__[arg1[2]] = valtype(arg1[3])
            else:
                obj.__dict__[arg1[2]] = arg1[3]
        elif type(eval(arg1[2])) == dict:
            obj = obj_dict["{}.{}".format(arg1[0], arg1[1])]
            for key, value in eval(arg1[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()       

    EOF = quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
