# `tinyscanner` - Un Scanner de Ports Simple en Python

## Table des matières

1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [Utilisation](#Utilisation)
4. [Explication du Code](#Code)
5. [Contributions](#Contributions)
6. [Licence](#Licence)

## Introduction

`tinyscanner` est un scanner de ports simple écrit en Python, conçu pour scanner les ports TCP et UDP sur une machine cible. Inspiré de Nmap, cet outil permet de vérifier quels ports sont ouverts et d'identifier les services associés.


## Installation

Pour installer `tinyscanner`, vous aurez besoin de cloner le dépôt et d'utiliser le Makefile pour installer la commande.

1. ### Cloner le dépôt
```sh
git clone https://github.com/YoannLetacq/active.git
cd active
```

2. ### Installer les dépendances

Assurez-vous d'avoir Python installé sur votre machine.

3. ### Installer la commande `tinyscanner`
```sh
make install
```

4. ### Pour désinstaller la commande `tinyscanner`
```sh
make uninstall
```

## Utilisation

Une fois installé, vous pouvez utiliser tinyscanner pour scanner les ports TCP et UDP.

### Afficher l'aide
```sh
tinyscanner --help
```

### Scanner un port TCP
```sh
tinyscanner -t [HOST] -p [PORT]
```
Exemple :
```sh
tinyscanner -t example.com -p 80
```

### Scanner un port UDP
```sh
tinyscanner -u [HOST] -p [PORT]
```

Exemple :
```sh
tinyscanner -u 8.8.8.8 -p 53
```

### Scanner une plage de ports TCP
```sh 
tinyscanner -t [HOST] -p [START_PORT]-[END_PORT]
```
Exemple :
```sh
tinyscanner -t example.com -p 80-82
```

### Scanner une plage de ports UDP
```sh
tinyscanner -u [HOST] -p [START_PORT]-[END_PORT]
```
Exemple :
```sh
tinyscanner -u example.com -p 80-82
```

## Explication du Code

1. ### `main.py`
- Contient les paramètres codés en dur et appelle `main_cli.py` pour la gestion des arguments de la ligne de commande.

2. ### `main_cli.py`
- Gère les arguments de la ligne de commande à l'aide de `argparse` et appelle les fonctions de scan appropriées.

3. ### `scan_tcp.py`
- Contient la fonction `scan_tcp` qui scanne les ports TCP et identifie les services associés.

4. ### `scan_udp.py`
- Contient la fonction `scan_udp` qui scanne les ports UDP et identifie les services associés.

5. ### `get_service.py`
Contient la fonction `get_service_name` qui retourne le nom du service associé à un port.

6. ### `Makefile`
- Fichier pour l'installation et la désinstallation de la commande `tinyscanner`.

## Contributions
Les contributions sont les bienvenues ! Pour proposer des améliorations, veuillez ouvrir une "issue" ou soumettre une "pull request" sur le dépôt GitHub.

## Authors
YoannLetacq