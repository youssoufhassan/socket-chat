# Socket Chat — Communication client-serveur en Python

Application de communication **client-serveur développée en Python**, mettant en œuvre des communications réseau bas niveau avec des **sockets** ainsi qu'un mécanisme de **RPC (Remote Procedure Call)**.

Le projet a pour objectif de mettre en pratique la communication entre plusieurs processus sur un réseau, la sérialisation des messages et la séparation entre les différentes couches de communication.

---

## Présentation

L'application repose sur une architecture client-serveur :

```text id="wq4m0e"
┌──────────────┐
│    Client    │
│  client.py   │
└──────┬───────┘
       │
       │ Communication réseau
       │
       ▼
┌──────────────┐
│    Serveur   │
│  server.py   │
└──────────────┘
```

Les échanges réseau sont structurés autour de plusieurs composants responsables de la communication, des messages RPC et de leur représentation.

---

## Fonctionnalités principales

Le projet met en œuvre :

* communication client-serveur ;
* utilisation des sockets Python ;
* transmission de messages sur le réseau ;
* mécanisme RPC ;
* sérialisation et désérialisation des données ;
* gestion des messages réseau ;
* séparation entre communication réseau et logique RPC.

---

## Architecture du projet

```text id="v0c1dj"
socket-chat/
│
├── client.py
├── server.py
│
├── rpcbind.py
├── rpcmsg.py
├── rpcnet.py
├── xdr.py
│
├── README.md
└── .gitignore
```

### `client.py`

Implémente la partie cliente de l'application.

Le client établit la communication avec le serveur et utilise les mécanismes de communication définis dans le projet pour échanger des données.

### `server.py`

Implémente la partie serveur.

Le serveur attend les connexions des clients et traite les communications entrantes.

### `rpcbind.py`

Gère les éléments liés à l'association et à la gestion des services RPC.

### `rpcmsg.py`

Contient la logique liée à la représentation et au traitement des messages RPC.

### `rpcnet.py`

Regroupe les mécanismes nécessaires aux communications réseau utilisées par le système RPC.

### `xdr.py`

Implémente les mécanismes liés à **XDR (External Data Representation)** pour représenter et échanger les données de manière structurée.

---

## Technologies

| Technologie  | Utilisation                                |
| ------------ | ------------------------------------------ |
| **Python 3** | Langage principal                          |
| **Sockets**  | Communication réseau                       |
| **RPC**      | Appels de procédures à distance            |
| **XDR**      | Représentation / sérialisation des données |

Le projet utilise principalement les fonctionnalités réseau et de communication disponibles dans l'écosystème Python.

---

## Fonctionnement

Le fonctionnement général peut être résumé ainsi :

```text id="g3gdyd"
             CLIENT
                │
                │
                ▼
        ┌───────────────┐
        │ Communication │
        │    réseau     │
        └───────┬───────┘
                │
                ▼
          Messages RPC
                │
                ▼
        ┌───────────────┐
        │ Sérialisation │
        │     XDR       │
        └───────┬───────┘
                │
                ▼
             SERVEUR
```

Les données sont préparées avant leur transmission et interprétées côté réception afin de permettre la communication entre le client et le serveur.

---

## Prérequis

Pour exécuter le projet, il est nécessaire d'avoir :

* **Python 3**
* un environnement permettant les communications réseau locales ;
* un terminal.

Vérifier l'installation de Python :

```bash
python --version
```

ou :

```bash
python3 --version
```

---

## Installation

Cloner le dépôt :

```bash
git clone <URL_DU_PROJET>
cd socket-chat
```

Aucune dépendance externe particulière n'est indiquée dans le dépôt actuel.

---

## Exécution

### 1. Démarrer le serveur

Dans un premier terminal :

```bash
python server.py
```

ou :

```bash
python3 server.py
```

### 2. Démarrer le client

Dans un second terminal :

```bash
python client.py
```

Le client peut alors communiquer avec le serveur selon le protocole défini par l'application.

> Les paramètres réseau utilisés par le client et le serveur doivent être cohérents avec la configuration du projet.

---

## Concepts mis en pratique

Ce projet permet de travailler concrètement sur plusieurs concepts de programmation système et réseau :

### Programmation réseau

* sockets ;
* communication client-serveur ;
* échanges de données ;
* gestion des connexions.

### RPC

Le projet met en œuvre le principe de **Remote Procedure Call**, permettant à un programme client de solliciter une opération exécutée à distance par un serveur.

### Sérialisation

Les données échangées doivent être représentées sous une forme pouvant être transmise sur le réseau.

Le projet utilise pour cela une représentation inspirée de **XDR (External Data Representation)**.

### Architecture en couches

Les différents fichiers séparent les responsabilités :

```text id="j6x6co"
Application
     │
     ▼
    RPC
     │
     ▼
 Messages
     │
     ▼
 Réseau
     │
     ▼
  Sockets
```

Cette séparation facilite la compréhension et l'évolution du système.

---

## Compétences développées

Ce projet m'a permis de travailler notamment sur :

* programmation Python ;
* programmation réseau ;
* sockets TCP/IP ;
* architecture client-serveur ;
* RPC ;
* sérialisation de données ;
* protocoles de communication ;
* conception de modules réseau ;
* débogage de communications entre processus.

---

## Structure technique

```text id="4b7v3a"
client.py
    │
    ├── Communication avec le serveur
    │
    └── Utilisation des mécanismes RPC
             │
             ▼
        rpcmsg.py
             │
             ▼
        rpcnet.py
             │
             ▼
          xdr.py
             │
             ▼
       Communication réseau
             │
             ▼
        server.py
```

---

## Projet

Projet réalisé dans le cadre de la formation en **L3 Informatique — Université de Bordeaux**.

### Auteur

**Youssouf Hassan**

Étudiant en informatique — Université de Bordeaux.

---

## Statut

**Projet fonctionnel — projet d'apprentissage en programmation réseau et systèmes distribués.**
