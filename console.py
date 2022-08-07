#!/usr/bin/python3

"""
Module console

Contain class Console
"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """A siple command interpreter

    Attributes
    ----------
    prompt : str
        A prompt text

    methods
    -------
    do_quit(line)
        Quit command to exit the program
    do_EOF(line)
        Exit on Ctrl-D
    emptyline()
        Overwrite default behavior to repeat last cmd
    do_create(line)
        create a new object
    do_show(line)
        Prints the string representation of an instance
    do_destroy(line)
        Deletes an instance based on the class name and id
    do_all(line)
        Prints all string representation of all instances
        based or not on the class name
    do_update(line)
        Updates an instance based on the class name and id by adding
        or updating attribute
    dfault(line)
        Accepts class name followed by arguement
    parse(line)
        parse user typed input and change tuple
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print("")
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(slef, line):
        """Creates an instance of class"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        else:
            instance = storage.class_dict[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = parse(line)
        if line == "" or line is None:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = parse(line)
        if line == "" or line is None:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if line != "":
            args = parse(line)
            if args[0] not in storage.class_dict:
                print("** class doesn't exist **")
            else:
                list_obj = [str(val) for ke, val in storage.all().items()
                            if val.__class__.__name__ == args[0]]
                print(list_obj)
        else:
            list_obj = [str(val) for key, val in storage.all().items()]
            print(list_obj)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        """
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            attr_update = args[3]
            attr_update = attr_update.strip("'")
            attr_update = attr_update.strip('"')
            setattr(storage.all()[key], args[2], cast(attr_update))
            storage.all()[key].save()
        elif len(line) == 0:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """Display number of instance specified"""
        args = parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        else:
            count = [key for key, val in storage.all().items()
                     if key.startswith(args[0] + ".")]
            print(len(count))

    def default(self, line):
        """Accepts class name followed by arguement"""
        args = tuple(line.split("."))
        class_argv = args[0]
        if len(args) == 1:
            print(f"*** Unknown syntax: {line}")
            return
        try:
            args = args[1].split("(")
            command = args[0]
            if command == "all":
                self.do_all(class_arg)
            elif command == "count":
                self.do_count(class_arg)
            elif command == "show":
                args = args[1].strip(")")
                arg_id = args.strip("'")
                arg_id = args.strip('"')
                line = f"{class_arg} {arg_id}"
                self.do_show(line)
            elif command == "destroy":
                args = args[1].strip(")")
                arg_id = args.strip("'")
                arg_id = args.strip('"')
                line = f"{class_arg} {arg_id}"
                self.do_destroy(line)
            elif command == "update":
                args = args[1].strip(")")
                args = args.split(", ")
                arg_id = args[0].strip("'")
                arg_id = arg_id.strip('"')
                arg_attr = args[1].strip("'")
                arg_attr = args[1].strip('"')
                arg_val = args[2]
                line = f"{class_arg} {arg_id} {arg_attr} {arg_val}"
                self.do_update(line)
            else:
                print(f"*** Unknown syntax: {line}")
        except IndexError:
            print(f"*** Unknown syntax: {line}")

    def parse(line):
        """Helper method to parse user typed input

        Returns
        -------
        tuple
            a list of user typed string
        """
        return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
