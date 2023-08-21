import json
from os.path import exists

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        k = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[k] = obj

    def save(self):
        s = {}
        for k, v in self.__objects.items():
            s[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(s, f)

    def reload(self):
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                ds = json.load(f)
                for k, v in ds.items():
                    FileStorage.__objects[k] = eval(v["__class__"])(**v)