#!/usr/bin/python3

# RPC Server (UDP)
# Implémentation d'un serveur RPC pour le test

import sys
import socket
import xdr      # Module fourni par l'enseignant
import rpcnet   # Module fourni par l'enseignant
import rpcmsg   # Module fourni par l'enseignant
import rpcbind  # Module fourni par l'enseignant

###############################################
###              CONSTANTES                  ###
###############################################

# Programme RPC, version et procédures
TEST_PROG = 0x20000001
TEST_VERS = 1

PROC_NULL = 0
PROC_PI = 1
PROC_INC = 2
PROC_ADD = 3
PROC_ECHO = 4

###############################################
###             PROCEDURES                   ###
###############################################

def proc_null(xid, prog, vers, proc, args):
    """Procédure qui ne fait rien et ne renvoie rien."""
    return b''

def proc_pi(xid, prog, vers, proc, args):
    """Procédure qui retourne la valeur de Pi (3.1415926)."""
    pi_value = 3.141592653589793
    return xdr.encode_double(pi_value)

def proc_inc(xid, prog, vers, proc, args):
    """Procédure qui retourne x + 1."""
    number = xdr.decode_int(args) 
    incremented_number = number + 1
    return xdr.encode_int(incremented_number)

def proc_add(xid, prog, vers, proc, args):
    """Procédure qui retourne x + y."""
    num1, num2 = xdr.decode_two_int(args)  
    result = num1 + num2
    return xdr.encode_int(result)

def proc_echo(xid, prog, vers, proc, args):
    """Procédure qui retourne la chaîne de caractères reçue."""
    return args

###############################################
###                 MAIN                    ###
###############################################

if len(sys.argv) != 2:
    print("Usage: server.py <port>")
    sys.exit(1)

host = ''  
port = int(sys.argv[1])

sserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    sserver.bind((host, port))  
    print(f"Serveur en écoute sur le port {port}...")
except Exception as e:
    print(f"Erreur lors de la liaison du socket au port {port}: {e}")
    sys.exit(1)

def handle_request(xid, prog, vers, proc, args):
    """Gestion des requêtes selon le type de procédure"""
    if proc == PROC_NULL:
        return proc_null(xid, prog, vers, proc, args)
    elif proc == PROC_PI:
        return proc_pi(xid, prog, vers, proc, args)
    elif proc == PROC_INC:
        return proc_inc(xid, prog, vers, proc, args)
    elif proc == PROC_ADD:
        return proc_add(xid, prog, vers, proc, args)
    elif proc == PROC_ECHO:
        return proc_echo(xid, prog, vers, proc, args)
    else:
        print(f"Procédure {proc} inconnue.")
        return b''


xid = 1234 
if not rpcbind.register(xid, TEST_PROG, TEST_VERS, port):
    print("Échec de l'enregistrement du programme dans rpcbind.")
    sys.exit(1)
else:
    print(f"Programme {TEST_PROG} enregistré avec rpcbind sur le port {port}.")

while True:
    try:
        sserver.settimeout(100) 
        data, client_adr = sserver.recvfrom(rpcnet.MAXMSG)  
        xid, prog, vers, proc, args = rpcmsg.decode_call(data)  
        print(f"Requête reçue: xid={xid}, prog={prog}, vers={vers}, proc={proc}")
        
        response_data = handle_request(xid, prog, vers, proc, args)
        encoded_response = rpcmsg.encode_reply(xid, response_data)
        
        sserver.sendto(encoded_response, client_adr)
        print(f"Réponse envoyée à {client_adr}")

    except socket.timeout:
        print("Timeout: Aucune requête reçue dans le délai imparti.")
    except Exception as e:
        print(f"Erreur lors du traitement de la requête: {e}")
sserver.close()
