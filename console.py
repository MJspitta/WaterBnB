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
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            try:
                x = eval(arg)()
                x.save()
                print(x.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        a = arg.split()
        if not a:
            print("** class name missing **")
        else:
            cl_name = a[0]
            if cl_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
            elif len(a) < 2:
                print("** instance id missing **")
            else:
                di = storage.all()
                k = f"{cl_name}.{a[1]}"
                if k in di:
                    print(di[k])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        a = arg.split()
        if not a:
            print("** class name missing **")
        else:
            cl_name = a[0]
            if cl_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
            elif len(a) < 2:
                print("** instance id missing **")
            else:
                di = storage.all()
                k = f"{cl_name}.{a[1]}"
                if k in di:
                    del di[k]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        di = storage.all()
        if not arg:
            print([str(v) for v in di.values()])
        else:
            a = arg.split()
            if a[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
            else:
                print([str(v) for k, v in di.items() if k.startswith(a[0])])
    
    def do_update(self, arg):
        a = arg.split()
        if not a:
            print("** class name missing **")
        else:
            cl_name = a[0]
            if cl_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
            elif len(a) < 2:
                print("** instance id missing **")
            else:
                di = storage.all()
                k = f"{cl_name}.{a[1]}"
                if k not in di:
                    print("** no instance found **")
                elif len(a) < 3:
                    print("** dictionary missing **")
                else:
                    i = di[k]
                    try:
                        di_rep = eval(a[2])
                    except (NameError, SyntaxError):
                        print("** invalid dictionary **")
                        return
                    if type(di_rep) is not di:
                        print("** invalid dictionary **")
                        return

                    for ky, v in di_rep.items():
                        if ky not in ["id", "created_at", "updated_at"]:
                            setattr(i, ky, v)
                    i.save()

    def do_count(self, arg):
        c = 0
        cl_names = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not arg:
            print("** class name missing **")
        elif arg not in cl_names:
            print("** class doesn't exist **")
        else:
            di = storage.all()
            for k in di.keys():
                if k.startswith(arg):
                    c += 1
            print(c)


if __name__ == '__main__':
    HBNBCommand().cmdloop()