import hashlib
import hmac
try:
    import cPickle as pickle
except:
    import pickle
import pprint
from StringIO import StringIO


def make_digest(message):
    "Return a digest for the message."
    return hmac.new('secret-shared-key-goes-here', message, hashlib.sha1).hexdigest()


class SimpleObject(object):
    "A very simple class to demonstrate checking digests before unpickling."
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
