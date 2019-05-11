from abc import ABCMeta,abstractmethod


class interface(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def do_GET(self, handler, param=None):
        pass

    def do_POST(self, handler, data=None):
        pass