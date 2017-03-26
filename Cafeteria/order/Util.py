
"""
This class is created to maintain all the util methods here.
For example : checking for null or any kind of sanitization
of the input arg happens here through many util functions
"""
#author : rajesh


class Util(object):

    @staticmethod
    def is_null(pObject):
        if pObject is None:
            return True
        else:
            return False
