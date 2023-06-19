#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a square"""
        sq = "[Square] ({}) {}/{} - ".format(self.id, self.x, self.y)
        str_s = "{}".format(self.width)
        return (sq + str_s)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args is not None and len(args) != 0:
            list_attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if list_attr[i] == 'size':
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionnary(self):
        """ Returns a dictionary with attributes """
        list_attr = ['id', 'size', 'x', 'y']
        dic = {}

        for key in list_attr:
            if key == 'size':
                dic[key] = getattr(self, 'width')
            else:
                dic[key] = getattr(self, key)

        return dic
