#!/usr/bin/python3
"""Package that contains the parent class of all
the sub classes that will be created later
"""
import json
import os
import csv


class Base:
    """Base class for all sub classes of the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_obj = []

        for index in range(len(list_cls)):
            list_obj.append(cls.create(**list_cls[index]))

        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialises in CSV file"""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = [0, 0, 0, 0]
            list_keys = ['id', 'size', 'x', 'y']

        mat = []
        if list_objs:
            for obj in list_objs:
                for i in range(len(list_keys)):
                    list_dic[i] = obj.to_dictionary()[list_keys[i]]
                mat.append(list_dic[:])

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(mat)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialises the CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            list_rows = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        mat = []
        for row in list_rows:
            dic_row = {}
            for elt in enumerate(row):
                dic_row[list_keys[elt[0]]] = int(elt[1])
            mat.append(dic_row)

        list_objs = []
        for i in range(len(mat)):
            list_objs.append(cls.create(**mat[i]))

        return list_objs
