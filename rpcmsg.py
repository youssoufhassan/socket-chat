#!/usr/bin/python3

# RPC Message Module
# Author(s):

import xdrlib

###############################################
###             RPC CONSTANTS               ###
###############################################

CALL = 0
REPLY = 1
RPC_VERSION = 2
AUTH_NONE = 0
MSG_ACCEPTED = 0
MSG_DENIED = 1
SUCCESS = 0

###############################################
###             ENCODE CALL                 ###
###############################################

def encode_call(xid, prog, vers, proc, data) -> bytes:
    """
    >>> encode_call(1, 1, 1, 1, b'ABCD').hex()
    '0000000100000000000000020000000100000001000000010000000000000000000000000000000041424344'
    """
    msg = b''
    # todo
    p = xdrlib.Packer()
    try:
        p.pack_uint(xid)
        p.pack_uint(CALL)
        p.pack_uint(RPC_VERSION)
        p.pack_uint(prog)
        p.pack_uint(vers)
        p.pack_uint(proc)
        p.pack_uint(AUTH_NONE)
        p.pack_uint(0)
        p.pack_uint(AUTH_NONE)
        p.pack_uint(0)
        
    except xdrlib.ConversionError as instance:
        print('packing failed:', instance.msg)
    msg= p.get_buffer() +data
    return msg

###############################################
###             ENCODE REPLY                ###
###############################################

def encode_reply(xid, data) -> bytes:
    """
    >>> encode_reply(1, b'ABCD').hex()
    '00000001000000010000000000000000000000000000000041424344'
    """
    msg = b''
    # todo
    p = xdrlib.Packer()
    try:
        p.pack_uint(xid)
        p.pack_uint(REPLY)
        p.pack_uint(MSG_ACCEPTED)
        p.pack_uint(AUTH_NONE)
        p.pack_uint(0)
        p.pack_uint(SUCCESS)
    except xdrlib.ConversionError as instance:
        print('packing failed:', instance.msg)
    msg= p.get_buffer() +data
   
    return msg

###############################################
###            DECODE CALL                  ###
###############################################

def decode_call(msg : bytes):
    """
    >>> msg = bytes.fromhex('0000000100000000000000020000000100000001000000010000000000000000000000000000000041424344') ; decode_call(msg)
    (1, 1, 1, 1, b'ABCD')
    """
    xid = prog = vers = proc = 0
    data = b''
    # todo
    p = xdrlib.Unpacker(msg)
    try:
        xid=p.unpack_uint()
        p.unpack_uint()
        p.unpack_uint()
        prog=p.unpack_uint()
        vers=p.unpack_uint()
        proc=p.unpack_uint()
        p.unpack_uint()
        p.unpack_uint()
        p.unpack_uint()
        p.unpack_uint()
    except xdrlib.ConversionError as instance:
         print('packing failed:', instance.msg)
    data=p.get_buffer()[p.get_position():]
    return (xid, prog, vers, proc, data)

###############################################
###             DECODE REPLY                ###
###############################################

def decode_reply(msg):
    """
    >>> msg = bytes.fromhex('00000001000000010000000000000000000000000000000041424344') ; decode_reply(msg)
    (1, b'ABCD')
    """
    xid = 0
    data = b''
    # todo
    p = xdrlib.Unpacker(msg)
    try:
        xid=p.unpack_uint()
        p.unpack_uint()
        p.unpack_uint()
        p.unpack_uint()
        p.unpack_uint()
        p.unpack_uint()
    except xdrlib.ConversionError as instance:
         print('packing failed:', instance.msg)
    data=p.get_buffer()[p.get_position():]
    return (xid, data)

###############################################
###                MAIN                     ###
###############################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF