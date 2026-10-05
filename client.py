#!/usr/bin/python3

import sys
import socket
import xdr      # Module fourni par l'enseignant
import rpcmsg   # Module fourni par l'enseignant
import rpcnet   # Module fourni par l'enseignant

# Programme RPC, version et procédures
TEST_PROG = 0x20000001
TEST_VERS = 1

PROC_NULL = 0
PROC_PI = 1
PROC_INC = 2
PROC_ADD = 3
PROC_ECHO = 4

def send_request(server_address, prog, vers, proc, args):
    """Envoie une requête au serveur RPC et retourne la réponse."""
    # Nous devons peut-être inclure un argument "data" ou des informations sur la requête.
    # Essayons de passer "args" comme le contenu de la requête.
    try:
        request_data = rpcmsg.encode_call(prog, vers, proc, args)  # Vérifier ici si encode_call() prend un argument supplémentaire
    except TypeError as e:
        print(f"Erreur lors de l'encodage de la requête: {e}")
        return None

    # Création du socket UDP pour envoyer la requête
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Envoi de la requête au serveur
        client_socket.sendto(request_data, server_address)
        
        # Réception de la réponse
        response_data, _ = client_socket.recvfrom(rpcnet.MAXMSG)
        # Décoder la réponse du serveur
        return rpcmsg.decode_reply(response_data)
    finally:
        client_socket.close()

def test_proc_pi(server_address):
    """Test de la procédure PI"""
    print("Envoi de la requête PI...")
    response = send_request(server_address, TEST_PROG, TEST_VERS, PROC_PI, b'')
    if response:
        print(f"Réponse de PI : {response}")
    else:
        print("Erreur dans la réponse de PI.")

def test_proc_inc(server_address, number):
    """Test de la procédure INC"""
    print(f"Envoi de la requête INC avec le nombre {number}...")
    response = send_request(server_address, TEST_PROG, TEST_VERS, PROC_INC, xdr.encode_int(number))
    if response:
        print(f"Réponse de INC : {response}")
    else:
        print("Erreur dans la réponse de INC.")

def test_proc_add(server_address, num1, num2):
    """Test de la procédure ADD"""
    print(f"Envoi de la requête ADD avec les nombres {num1} et {num2}...")
    response = send_request(server_address, TEST_PROG, TEST_VERS, PROC_ADD, xdr.encode_two_int(num1, num2))
    if response:
        print(f"Réponse de ADD : {response}")
    else:
        print("Erreur dans la réponse de ADD.")

def test_proc_echo(server_address, message):
    """Test de la procédure ECHO"""
    print(f"Envoi de la requête ECHO avec le message '{message}'...")
    response = send_request(server_address, TEST_PROG, TEST_VERS, PROC_ECHO, message.encode('utf-8'))
    if response:
        print(f"Réponse de ECHO : {response.decode('utf-8')}")
    else:
        print("Erreur dans la réponse de ECHO.")

if __name__ == "__main__":
    # Vérification de la ligne de commande
    if len(sys.argv) != 3:
        print("Usage: client.py <server_ip> <port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])

    # Adresse du serveur (le client se connecte à l'adresse IP et au port du serveur)
    server_address = (server_ip, port)

    # Test des différentes procédures
    test_proc_pi(server_address)
    test_proc_inc(server_address, 5)
    test_proc_add(server_address, 10, 20)
    test_proc_echo(server_address, "Bonjour, serveur RPC!")
