#!/usr/bin/python3
''' Module that contains prompt '''
import cmd
import sys
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import models


class HBNBCommand(cmd.Cmd):
    '''
        Class for console:
        create, show, destroy
        all, update
    '''

    prompt = "(hbnb) "
    allclass = [
                'BaseModel', 'User', 'State',
                'City', 'Place', 'Amenity',
                'Review'
                ]

    def do_quit(self, args):
        ''' Quit command to exit the program '''
        return True

    def do_EOF(self, args):
        ''' Handle ctrl + d signal '''
        return True

    def emptyline(self):
        ''' Just empty line '''
        pass

    def default(self, line):
        ls = line.split('.')
        if ls[0] in self.allclass:
            if ls[1] == 'all()':
                self.do_all(ls[0])
            elif ls[1] == 'count()':
                all_objs = models.storage.all()
                counter = 0
                for k, v in all_objs.items():
                    if ls[0] in k:
                        counter += 1
                print(counter)
            elif 'show' in ls[1] and "\"" in ls[1]:
                new_ls = ls[1].split('\"')
                if 'show' in new_ls[0]:
                    st = ls[0] + ' ' + new_ls[1]
                    self.do_show(st)
            elif 'destroy' in ls[1] and "\"" in ls[1]:
                new_ls = ls[1].split('\"')
                if 'destroy' in new_ls[0]:
                    st = ls[0] + ' ' + new_ls[1]
                    self.do_destroy(st)
            elif 'update' in ls[1]:
                st = ls[1].replace(',', '.')
                st = st.replace('update(', '')
                st = st.replace(')', '')
                st = st.replace('\"', '')
                st = st.replace(' ', '')
                st = st.replace('.', ' ')
                fst = ls[0] + ' ' + st
                self.do_update(fst)
            else:
                return cmd.Cmd.default(self, line)
        else:
            return cmd.Cmd.default(self, line)

    def do_create(self, class_name):
        '''
            Create a new instance of class name given
            usage: create [classname]
        '''
        if not class_name:
            print('** class name missing **')
        elif class_name not in HBNBCommand.allclass:
            print("** class doesn't exist **")
        else:
            new = eval(class_name)()
            new.save()
            print(new.id)

    def do_show(self, line):
        '''
            show instance of class by id
            usage: show [classname] [id]
        '''
        command = line.split()
        if not command:
            print('** class name missing **')
            return
        if command[0] not in HBNBCommand.allclass:
            print("** class doesn't exist **")
            return
        elif len(command) < 2:
            print("** instance id missing **")
            return
        else:
            concat = command[0] + '.' + command[1]
            all_objs = models.storage.all()
            cnt = 0
            for key, value in all_objs.items():
                if concat == key:
                    print(value)
                    cnt += 1
            if cnt == 0:
                print('** no instance found **')

    def do_destroy(self, line):
        '''
            Destroy instance of class by id
            usage: destroy [classname] [id]
        '''
        command = line.split()
        if not command:
            print('** class name missing **')
            return
        if command[0] not in HBNBCommand.allclass:
            print("** class doesn't exist **")
            return
        elif len(command) < 2:
            print("** instance id missing **")
            return
        else:
            concat = command[0] + '.' + command[1]
            all_objs = models.storage.all()
            cnt = 0
            for key, value in all_objs.items():
                if concat == key:
                    del all_objs[concat]
                    models.storage.save()
                    cnt += 1
                    return
            if cnt == 0:
                print('** no instance found **')

    def do_all(self, cls_name):
        '''
            Prints all string representation of all
            instances based or not on the class name.
            Ex: $ all BaseModel or $ all.
        '''
        all_objs = models.storage.all()
        l_eq = []
        if cls_name and cls_name not in HBNBCommand.allclass:
            print("** class doesn't exist **")
        elif cls_name and cls_name in HBNBCommand.allclass:
            for key, value in all_objs.items():
                if cls_name in key:
                    l_eq.append(value.__str__())
            if len(l_eq):
                print(l_eq)
        else:
            for key, value in all_objs.items():
                l_eq.append(value.__str__())
            if len(l_eq):
                print(l_eq)

    def do_update(self, line):
        '''
            update instance of class by id
            usage: [update] [classname] [id] [attr] [value]
        '''
        command = line.split()
        all_objs = models.storage.all()
        if not command:
            print('** class name missing **')
            return
        if command[0] not in HBNBCommand.allclass:
            print("** class doesn't exist **")
            return
        elif len(command) < 2:
            print("** instance id missing **")
            return
        elif len(command) < 3:
            print("** attribute name missing **")
            return
        elif len(command) < 4:
            print("** value missing **")
            return
        else:
            concat = command[0] + '.' + command[1]
            cnt = 0
            for key in all_objs:
                if concat == key:
                    setattr(all_objs[key], command[2], command[3])
                    cnt += 1
            if cnt == 0:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
