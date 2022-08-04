#! /usr/bin/python3
"""
    Define Console class
"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Command interpreter for AirBnB project
    """

    prompt = '(hbnb) '
    __class_name = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Amenity.__name__: Amenity,
        Place.__name__: Place,
        Review.__name__: Review
    }

    def do_quit(self, line):
        """
            Exit the console
        """

        return True

    def do_EOF(self, line):
        """
            Exit the console
        """

        return True

    def emptyline(self):
        """
            an empty line + ENTER shouldn’t execute anything
        """
        pass

    @staticmethod
    def parse(line):
        """
            Split all arguments and return a list
        """

        if len(line) == 0:
            return []
        return line.split(' ')

    def do_create(self, line):
        """
            Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id.
            Ex: $ create BaseModel
        """
        line_list = HBNBCommand.parse(line)
        if len(line_list) == 0:
            print('** class name missing **')
        else:
            if line_list[0] not in HBNBCommand.__class_name.keys():
                print('** class doesn\'t exist **')
            else:
                brand_new = HBNBCommand.__class_name[line_list[0]]()
                brand_new.save()
                print(brand_new.id)

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
        """

        line_list = HBNBCommand.parse(line)
        if len(line_list) == 0:
            print('** class name missing **')
        else:
            if line_list[0] in HBNBCommand.__class_name.keys():
                if len(line_list) >= 2:
                    # data = storage.all()
                    if f'{line_list[0]}.{line_list[1]}'\
                       in storage.all().keys():
                        print(storage.all()[f'{line_list[0]}.{line_list[1]}'])
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name
            and id (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234
        """

        line_list = HBNBCommand.parse(line)
        if len(line_list) == 0:
            print('** class name missing **')
        else:
            if line_list[0] in HBNBCommand.__class_name.keys():
                if len(line_list) >= 2:
                    storage.reload()
                    # data = storage.all()
                    if f'{line_list[0]}.{line_list[1]}'\
                       in storage.all().keys():
                        del storage.all()[f'{line_list[0]}.{line_list[1]}']
                        storage.save()
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')

    def do_all(self, line):
        """
            Prints all string representation of all instances
            based or not on the class name.
            Ex: $ all BaseModel or $ all
        """

        line_list = HBNBCommand.parse(line)
        if len(line_list) > 0 and\
           line_list[0] not in HBNBCommand.__class_name.keys():
            print('** class doesn\'t exist **')
        else:
            all_data = []
            for v in storage.all().values():
                if len(line_list) > 0 and line_list[0] == v.__class__.__name__:
                    all_data.append(v.__str__())
                elif len(line_list) == 0:
                    all_data.append(v.__str__())
            print(all_data)

    def do_update(self, line):
        """
            Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """

        line_list = HBNBCommand.parse(line)
        if len(line_list) == 0:
            print('** class name missing **')
        else:
            if line_list[0] in HBNBCommand.__class_name.keys():
                if len(line_list) >= 2:
                    d_index = f'{line_list[0]}.{line_list[1]}'
                    if d_index in storage.all().keys():
                        if len(line_list) >= 3:
                            if len(line_list) >= 4:
                                storage.all()[d_index]\
                                        .__dict__[line_list[2]]\
                                        = eval(line_list[3])
                                storage.save()
                            else:
                                print('** value missing **')
                        else:
                            print('** attribute name missing **')
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')

    @staticmethod
    def count(line):
        """
            Counts the number of instances of a class
        """

        count = 0
        storage.all()
        for v in storage.all().values():
            if line == v.__class__.__name__:
                count += 1

        print(count)

    def default(self, line):
        """
            Handles command with no method
        """
        try:
            args = line.split('.')
            cls_name = args[0]
            commands = args[1].replace('(', '')[:-1]
            cmd_name = commands.split('"')[0]

            if cmd_name == 'all':
                self.do_all(cls_name)
            elif cmd_name == 'count':
                HBNBCommand.count(cls_name)
            elif cmd_name == 'show':
                id = commands.split('"')[1]
                arg = ' '.join([cls_name, id])
                self.do_show(arg)
            elif cmd_name == 'destroy':
                id = commands.split('"')[1]
                arg = ' '.join([cls_name, id])
                self.do_destroy(arg)
            elif cmd_name == 'update':
                if '{' in commands:
                    id = commands.split('"')[1]
                    dict_d = commands.split('{')[1][:-1]
                    value = '{' + dict_d + '}'
                    dict_value = eval(value)
                    for k, v in dict_value.items():
                        if type(v) == int:
                            v = str(v)
                        v = '"' + v + '"'
                        arg = ' '.join([cls_name, id, k, v])
                        self.do_update(arg)
                else:
                    id = commands.split('"')[1]
                    attr = commands.split('"')[3]
                    value = commands.split(',')[2][1:]
                    arg = ' '.join([cls_name, id, attr, value])
                    self.do_update(arg)
            else:
                super().default(line)
        except Exception:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
