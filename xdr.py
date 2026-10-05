#!/usr/bin/python3
# Ignorer les avertissements de dépréciation
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# XDR Module
# Author(s): Hassan Youssouf Youssouf et Adoum Mahamat Tahir

import xdrlib

###############################################
###               XDR ENCODE                ###
###############################################

def encode_double(val) -> bytes:
    """
    >>> encode_double(1.2).hex()
    '3ff3333333333333'
    """
    data = b''
    # todo
    p = xdrlib.Packer()
    try:
        p.pack_double(val)
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    data =p.get_buffer()
    return data

def encode_int(val) -> bytes:
    """
    >>> encode_int(-1).hex()
    'ffffffff'
    """
    p = xdrlib.Packer()
    try:
        p.pack_int(val)
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    data = p.get_buffer()
    return data

def encode_uint(val) -> bytes:
    """
    >>> encode_uint(10).hex()
    '0000000a'
    """
    p = xdrlib.Packer()
    try:
        p.pack_uint(val)
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    data = p.get_buffer()
    return data

def encode_bool(val : bool) -> bytes:
    """
    >>> encode_bool(True).hex()
    '00000001'
    """
    data = b''
    # todo
    
    p = xdrlib.Packer()
    try:
        p.pack_bool(val)
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    data += p.get_buffer()
    return data

def encode_string(val: str) -> bytes:
    """
    >>> encode_string("hello").hex()
    '0000000568656c6c6f000000'
    """
    data = b''
    p = xdrlib.Packer()
    try:
        p.pack_string(val.encode('ascii'))
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    data = p.get_buffer()
    return data

def encode_two_int(val1, val2) -> bytes:
    """
    >>> encode_two_int(-1,2).hex()
    'ffffffff00000002'
    """
    
    data = b''
    p = xdrlib.Packer()
    c = xdrlib.Packer()
    try:
        p.pack_int(val1)
        c.pack_int(val2)
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    data += p.get_buffer()
    data +=c.get_buffer()
    return data

###############################################
###             XDR DECODE                  ###
###############################################

def decode_double(data : bytes):
    """
    >>> msg = bytes.fromhex('3ff3333333333333') ; decode_double(msg)
    1.2
    """
    # todo
    p = xdrlib.Unpacker(data)
    try:
        neymar = p.unpack_double()
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    return neymar


def decode_int(data : bytes):
    """
    >>> msg = bytes.fromhex('ffffffff') ; decode_int(msg)
    -1
    """
    # todo
    p = xdrlib.Unpacker(data)
    try:
        messi = p.unpack_int()
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    return messi

def decode_uint(data : bytes):
    """
    >>> msg = bytes.fromhex('00000001') ; decode_uint(msg)
    1
    """
    p = xdrlib.Unpacker(data)
    try:
        salah = p.unpack_uint()
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    return salah

def decode_bool(data : bytes):
    """
    >>> msg = bytes.fromhex('00000001') ; decode_bool(msg)
    True
    """
    # todo
    p = xdrlib.Unpacker(data)
    try:
        zidane = p.unpack_bool()
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    return zidane

def decode_string(data : bytes) -> str:
    """
    >>> msg = bytes.fromhex('0000000568656c6c6f000000') ; decode_string(msg)
    'hello'
    """
    # todo
    p = xdrlib.Unpacker(data)
    try:
        figo = p.unpack_string().decode('ascii')
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    return figo

def decode_two_int(data):
    """
    >>> msg = bytes.fromhex('ffffffff00000002') ; decode_two_int(msg)
    (-1, 2)
    """
    # todo
    p = xdrlib.Unpacker(data)
    try:
        mbappe,hakimi= p.unpack_int(),p.unpack_int()
    except xdrlib.ConversionError as instance:
         print('packing the double failed:', instance.msg)
    return mbappe,hakimi

###############################################
###                MAIN                     ###
###############################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
