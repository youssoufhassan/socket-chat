#!/usr/bin/python3

# RPC Net Module
# Author(s): Adoum Mahamat Tahir et Hassan youssouf youssouf

import socket
import rpcmsg

###############################################
###           CONSTANTS                     ###
###############################################

MAXMSG = 1500

###############################################
###                CALL UDP                 ###
###############################################

def call(host, port, xid, prog, vers, proc, args) -> bytes:
    result = b''
    # todo
    try:
        sclient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sclient.settimeout(5)
        data=rpcmsg.encode_call(xid, prog, vers, proc, args)
        sclient.sendto(data,(host, port))
        reply,_=sclient.recvfrom(MAXMSG)
        _,result=rpcmsg.decode_reply(reply)
    
        return result
    except Exception as e:
        print("ERROR: program failed!")

###############################################
###               REPLY UDP                 ###
###############################################

def reply(sserver, handle):
    # todo
    

    try:
        sserver.settimeout(5)
        data,client_adr=sserver.recvfrom(MAXMSG)
        xid, prog, vers, proc,args=rpcmsg.decode_call(data)
        msg=handle(xid, prog, vers, proc,args)
        encoded_msg=rpcmsg.encode_reply(xid,msg)
        sserver.sendto(encoded_msg,client_adr)
    except socket.timeout:
        print("Timeout: Aucune requête reçue dans le délai imparti.")
    except Exception as e:
        print("ERROR: program failed!")

    return
if __name__ == "__main__":
    import doctest
    doctest.testmod()
# EOF
