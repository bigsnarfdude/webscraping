import hmac
import hashlib
import array
import time


def HOTP(K, C, digits=6):
    """
    key K 
    counter C
    """
    C_bytes = _long_to_byte_array(C)
    hmac_sha1 = hmac.new(key=K, msg=C_bytes,
                         digestmod=hashlib.sha1).hexdigest()
    return Truncate(hmac_sha1)[-digits:]


def TOTP(K, digits=6, window=30):
    """
    30 second time expiration
    """
    C = long(time.time() / window)
    return HOTP(K, C, digits=digits)


def Truncate(hmac_sha1):
    """
    http://tools.ietf.org/html/rfc4226#section-5.3
    """
    offset = int(hmac_sha1[-1], 16)
    result = int(hmac_sha1[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
    return str(result)


def _convert_to_bytearray(long_num):
    """
    convert to bytearray
    """
    ba = array.array('B')
    for i in reversed(range(0, 8)):
        ba.insert(0, num & 0xff)
        num >>= 8
    return ba
