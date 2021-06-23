'''

Implement a data structure which carries out the following operations without resizing the underlying array:
add(value): Add a value to the set of values.
check(value): Check whether a value is in the set.
The check method may return occasional false positives (in other words, incorrectly identifying an element as part of
the set), but should always correctly identify a true element.

'''
import hashlib
from hashlib import md5, sha256
from binascii import unhexlify


class BloomFilter:
    def __init__(self):
        self.vector = 0

    def get_hash(self, value):
        hash_obj = hashlib.md5(value.encode("UTF-8")) # Hash it up baby
        readable = hash_obj.hexdigest() # Get a readable hash
        binary = unhexlify(readable) # Binary data of hexadecimal representation.
        inte = int.from_bytes(binary, byteorder='little')
        return inte

    def add(self, value):
        hash_val = self.get_hash(value)
        self.vector |= hash_val
        return self.vector

    def check(self, value):
        hashed = self.get_hash(value)
        for a, b in zip(bin(hashed)[2:], bin(self.vector)[2:]):
            if bool(int(a)) and not bool(int(b)):
                return False
        return True


if __name__ == '__main__':
    bf = BloomFilter()
    print(bf.vector)
    bf.add("test1")
    print(bf.vector)
    bf.add("test20")
    print(bf.vector)
    print(bf.check("test1"))
    print(bf.check("test20"))
