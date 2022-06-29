#!/usr/bin/env python3
""" module that contains the command interpreter """
import cmd
import json
from nntplib import ArticleInfo

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ defines command interpreter class """
    prompt = '(hbnb) '

    def do_create(self, args):
        'Creates new instance and saves it to JSON file\n'
        if not args:
            print("** class name missing **")
        elif args != BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args):
        'Prints a string representation of an instance, based on name and id\n'
        all_objs = storage.all()
        arg_list = args.split()
        if not arg_list:
            print("** class name is missing **")
        elif arg_list[0] != BaseModel.__name__:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            match = False
            for obj_id in all_objs.keys():
                if arg_list[1] == all_objs[obj_id].id:
                    print(all_objs[obj_id])
                    match = True
            if match is not True:
                print("** no instance found **")

    def do_update(self, args):
        arg_list = args.split()
        all_objs = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif args != BaseModel.__name__:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            
                    
    def do_quit(self, args):
        'Quit command to exit the program\n'
        exit()

    def do_EOF(self, args):
        'Quit command to exit the program\n'
        exit()

    def postcmd(self, stop, line):
        """ continues command interpreter after help """
        if cmd.Cmd.do_help:
            HBNBCommand().cmdloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
