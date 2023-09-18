#!/usr/bin/python3
"""
Module contains class Square
10. And now, the Square!
11. Square size
12. Square update
14. Square instance to dictionary representation
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)
        self.size = size

  
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

      @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        arg_names = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                if key in arg_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
