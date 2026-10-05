#!/usr/bin/python3
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#!/usr/bin/python3

# RPC Bind Module
# Author(s): 

import xdrlib
import xdr      # module fourni par le professeur dans VPL
import rpcnet   # module fourni par le professeur dans VPL
import rpcmsg   # module fourni par le professeur dans VPL

###############################################
###           CONSTANTS                     ###
###############################################

RPCB_HOST = "localhost"
RPCB_PORT = 111
RPCB_PROG = 100000 # rpcbind / portmap
RPCB_VERS = 4

RPCBPROC_SET = 1
RPCBPROC_UNSET = 2
RPCBPROC_GETADDR = 3

###############################################
###                GETPORT                  ###
###############################################
def getport(xid, prog, vers) -> int:
    """
    Récupère le port d'un programme RPC auprès de rpcbind.
    """
    port = -1
    try:
        args = xdr.encode_two_int(prog, vers)
        
        reply = rpcnet.call(RPCB_HOST, RPCB_PORT, xid, RPCB_PROG, RPCB_VERS, RPCBPROC_GETADDR, args)
        
        uaddr = xdr.decode_string(reply)
        
        ip_parts = uaddr.split('.')
        if len(ip_parts) == 6: 
            ip = '.'.join(ip_parts[:4])  
            port = int(ip_parts[4]) * 256 + int(ip_parts[5])  # Ca
            print(f"IP: {ip}, Port: {port}")  # Débogage pour vérifier les valeurs extraites
        else:
            print(f"Erreur dans le format de l'adresse universelle: {uaddr}")

    except Exception as e:
        print(f"Erreur lors de l'appel de getport : {e}")
    
    return port
###############################################
###                 REGISTER                ###
###############################################
def register(xid, prog, vers, port) -> bool:
    try:
        uaddr = f"127.0.0.1.{port // 256}.{port % 256}"
        netid = "udp"
        owner = ""
        args = xdr.encode_two_int(prog, vers) + xdr.encode_string(netid) + xdr.encode_string(uaddr) + xdr.encode_string(owner)
        reply = rpcnet.call(RPCB_HOST, RPCB_PORT, xid, RPCB_PROG, RPCB_VERS, RPCBPROC_SET, args)
        success = xdr.decode_bool(reply)
        return success
    except Exception as e:
        print(f"Erreur lors de l'enregistrement : {e}")
    return False
###############################################
###              UNREGISTER                 ###
###############################################
def unregister(xid, prog, vers) -> bool:
    try:
        args = xdr.encode_two_int(prog, vers) + xdr.encode_string("") + xdr.encode_string("") + xdr.encode_string("")
        reply = rpcnet.call(RPCB_HOST, RPCB_PORT, xid, RPCB_PROG, RPCB_VERS, RPCBPROC_UNSET, args)
        success = xdr.decode_bool(reply)
        return success
    except Exception as e:
        print(f"Erreur lors de la suppression de l'enregistrement : {e}")
    return False


# EOF
