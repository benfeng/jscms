__author__ = 'fengbq@live.com'
# 常量 const
import sys
class _const(object):
    class ConstError(TypeException): pass
    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise(self.ConstError, "Can't rebind const (%s)" % key)
        else:
            self.__dict__[key] = value
    def __getattr__(self, key):
        if self.__dict__.has_key(key):
            return self.key
        else:
            return None
sys.modules[__name__] = _const()