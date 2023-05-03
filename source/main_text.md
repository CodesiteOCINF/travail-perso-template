# Travail Personnel: Fonctionnement d'un Routeur 

```{figure} img/routeur_image.png
    :scale: 50 %
```
 ## Réseau: les bases

### Réseaux informatiques
On appelle réseau informatique une structure qui relie plusieurs machines informatiques entre elles afin de se transmettre de l'information via des signaux. Un réseau peut contenir diverses machines qui lui sont rattachées:

- Des clients/hôtes: c'est à dire des ordinateurs/téléphones/… Soit tout ce qui va s'attacher à un réseau afin de l'exploiter.
- Des serveurs : il s’agit d’une machine dont l’objectif est de répondre à des requêtes demandées par des clients.
- Des moyens de liaison : 
    * Via câble: électrique ou fibre optique
    * Sans câble (Wireless): transmission par émissions d'ondes électromagnétiques (antenne)
    
- Des intermédiaires directs, c'est à dire des machines dont le but est de faire office de relais (Hub/switch, router, ...)
Un exemple typique:

```{figure} img/exemple1.jpg
    :scale: 50 %
```

Dans ce schéma plusieurs machines (les ordinateurs et le serveur) sont reliées entre elles via des switchs. Un routeur va faire le pont entre les 2 LAN, ce qui permettrait (entre autre) l'accès de toutes les machines au serveur.


### Types de réseaux conventionnels
Ces réseaux se classifient (notamment) selon leurs portées, nous retiendrons les suivants:
- **PAN (Personnal Area Network):** Il s’agit d’un réseau reliant des appareils personnels sans grandes infrastructures (exemple : câble jack, Bluetooth, …)
- **LAN (Local Area Network) :** Cela consiste en une liaison (par câble) de plusieurs machines dans un même bâtiment (petites entreprises/ gymnase/ maison).
- **WLAN (Wireless Local Area Network) :** même chose que le LAN mais sans fils, souvent avec des routeur WIFI.
- **WAN (Wide Area Network) :** c’est un ensemble de réseaux reliés entre eux sur une grande distance (plusieurs villes/régions/pays), ils utilisent différents moyens de liaison. Par exemple une ville (moderne) est un WAN car elle va relier un nombre non-négligeable de (W)LAN ensemble (via des routeurs).



## Couches OSI
Afin de centrer le rôle des routeurs, nous devons détailler les différents points clés nécéssaires à la communication entre 2 machines. Pour se faire nous allons nous servir d'un modèle théorique que l'on appelle le modèle OSI (Open System Interconnection) qui va décomposer le tout en 7 couches (layers en anglais):

```{figure} img/OSI.png
    :scale: 50 %
```

Donnons un aperçut plus concret de ce modèle:
- Couche 1: Il s'agit de l'ensemble des dispositifs transportant physiquement l'information (câble/antenne).
- Couche 2: Le principe est de jouer le rôle d'interface avec la liaison physique, l'idée va être d'émettre les bits d'informations ou les capter dans des frames (cadre mémoire). Pour cela, l'on utilise des cartes réseaux (pour les câbles) ou des cartes wifi (pour les transmissions par ondes). Chacune de ses cartes possèdent ce que l'on appelle une adresse MAC, il s'agit d'une adresse fixe unique à chaque carte donné par le constructeur qui permet des transmissions de paquets entre cartes sans ambiguïté. La machine principale faisant le lien entre les cartes est le switch que nous détaillerons par la suite.
- Couche 3: Cette couche est responsable de la transmission des paquets jusqu'à leurs destinations, on se sert plus des adresses MAC mais des adresses IP (dont nous détaillerons la nature par la suite), c'est cette couche qui nous concernera car elle est assurée par les routeurs. (Adresse MAC varie lors du trajet mais pas IP)
- Couche 4: Son rôle est de catégoriser les flux de données pour les répartir dans des numéros de port de la machine réceptrice afin de distinguer différents types d'informations : par exemple, lorsque l'on utilise plusieurs applications online en parallèle (youtube et WhatsApp/...), pour chaque application il y aura un port (numérique) de réception bien défini afin d'éviter des mélanges d'informations.
- Couche 5-6-7: Tout le reste, autrement dit gérer les requêtes d'échange de données, interprétation des données, puis interface utilisateur.

En pratique c'est plutôt le modèle TCP/IP qui est utilisé, il s'agit du même modèle que l'OSI mais avec certaines couches qui sont fondues ensemble:
```{figure} img/ositcpip.png
    :scale: 50 %
```


## Machines intermédiaires

Souvent les machines que l'on achète sur internet sont des hybrides de plusieurs machines "élémentaires", détaillons les différents types existants (Li correspond à la couche i concernée):
- Répéteur: Sur de longue distance, les signaux peuvent devenir trop faible, donc on utilise un répétiteur afin de les dupliquer pour les amplifier. (L1)
- Le hub joue de rôle d’émetteur sans intelligence, autrement dit ce dernier reçoit une trame, il la renvoie sans distinction dans toutes les connexions périphériques. (LAN: L2)
- Le switch est un Hub mais intelligent dans la mesure ou il va reconnaître l'adresse Mac du destinataire dans les trames passant dans ses connexions, puis va renvoyer la trame uniquement sur la connexion entre lui et le destinataire.(LAN: L2)
- Le bridge: il s'agit d'une sorte de combinaison entre un switch et un routeur mais en moins évolué : l'idée est de relier un petit nombre de LAN en n'utilisant que les adresses MAC. (L2)
- Le routeur, quant à lui, va relier plusieurs (W)LAN ou des réseaux plus larges. Son rôle va être de lire les adresses IP de routage et en utilisant des tables de routages qui contiennent les adresses à ses alentours, il va envoyer le paquet sur une connexion, le faisant avancer plus loin. (L3)
- Un Modem: sert à convertir les messages digitaux en messages analogiques (et réciproquement), afin de permettre de communiquer sur le réseau. Concrètement cela consiste à passer de n'importe quel support physique entrant (wifi, câble, fibre optique, ...) à une sortie donnée. Fondamentalement il y a 3 sorties possibles: Ethernet, fibre optique ou câble coaxial. Cela dépendra de la nature du réseau à relier. (L2-L1)




### Adresse IP

Définition et concept

Internet protocol (IP), il s’agit d’une adresse le plus souvent temporaire permettant d’être identifié sur un réseau (adresse pour les paquets). Il existe 2 types d’adresses IP:
- IPv4: Il s'agit d'une adresse codée sur 4 fois 8 bits, néanmoins ce modèle a un défaut qui est que le nombre d'adresse possible vaut environ 4 milliards, ce qui n'est plus assez actuellement. En conséquent, l'IPv6 est née et un protocole a été mis en place pour permettre de vivre avec l'IPv4 malgré le surplus d'appareils.
- IPv6: C'est une adresse codée sur 8 champs de 16 bits (écrit en hexadécimal et séparé par des doubles-points lors des représentations).




### Protocole lié

**IPv4**

Il s'agit d'une manière d'assurer le routage, en mettant une en-tête àau sommet d'un paquet de données afin de détailler diverses informations pratiques pour son voyage sur les réseaux:

```{figure} img/ipv4.png
    :scale: 50 %
```


Détaillons les différents éléments:
- Version: Il s'agit du type d'adresse IP utilisé (Ipv4 ou 6).
- Header Length: longueur de l'en-tête en bit.
- Type de service: 
    - DSCP: Differentiated Services Code Point (différentie des services possible pour des paquets).
    - ECN: notification explicite de congestion (prévient la perte de paquets).
- Total Length: longueur en bit de la longueur du paquet en entier (en-tête comprise).
- Indentification: Il s'agit du nombre de fragments de paquets (comme les paquets emportent un nombre limité d'information, un message est envoyé via plusieurs paquets qui n'arrivent pas nécessairement dans le bon ordre). 
- Flags: Codé sur 3 bits, le premier ne sert à rien, le deuxième indique si le paquet peut être fragmenté pour faciliter le routage, le 3ème  dit s'il est le dernier fragment à arriver.
- Fragment Offset: Numéro indiquant la position du paquet.
- Time to Live: la durée de vie représente le nombre de routeur maximal par lequel il doit passer (à chaque passage, on soustrait 1 à ce nombre et quand il est à 0, alors le paquet doit être abandonné).
- Protocol: Il s'agit d'un numéro faisant référence au protocole de la couche 4 qui doit être utilisé pour le traitement du paquet (IMCP=1, TCP=6, UDP=17).
- Header Checksum: nombre représentant le total de l'en-tête (fragmentation) utilisé pour détecter d'éventuelles erreurs de transfert.
- Source IP Address: adresse IP de l’émetteur.
- Destination IP Address: adresse IP du récepteur.



**NAT:**
Afin de résoudre la problématique du manque d'adresse IPv4 sans tout changer, une solution a été proposé et c'est de suivre le processus NAT (Network Address Translation). Le NAT propose de séparer les réseaux privés (maison, entreprise, ...) des réseaux publics (internet principalement) pour y rajouter entre-deux un intermédiaire (routeur) qui va communiquer les requêtes "en son nom". Ainsi le principe utilisé est le suivant: les machines privées se servent d'une adresse IPv4 privée (non enregistré officiellement) et quand le paquet doit quitter le réseau privé, elle passe par un routeur qui va utiliser une adresse IPv4 publique, qui elle est valide sur le réseau, pour exécuter les requêtes et le routeur retiendra l'adresse IP privée/adresse publique temporaire utilisée qu'il associera à un port. Il existe 3 types de NAT qui correspondent à la manière d'associer les adresses:
- NAT statique: c'est le moins efficient: une adresse privée reliée avec une adresse publique.
- NAT dynamique: une adresse privée est associée quand cela est nécéssaire à une des adresses publiques du routeur (il en possède un nombre limité et elles se relaient). S'il devait à manquer une adresse publique, il va stocker le paquet et l'envoyer quand une place est libre. Le problème avec cette stratégie est qu'une machine externe ne peut initier une conversation avec une machine privée (car les paquets arriveraient uniquement au routeur et il ne saurait pas où les rediriger)
- PAT: Le routeur a pour une adresse IP publique, plusieurs ports accessible, ce qui permet à plusieurs adresses privées d'utiliser une adresse publique.

Un avantage du NAT est en terme de sécurité car en utilisant des adresses propres au routeur, on évite d'exposer celles des hôtes et donc des attaques ciblées sont rendues plus difficiles. Néanmoins il y a beaucoup de désavantages avec le NAT, entre-autre certains protocoles ne peuvent plus marcher avec cet effet pare-feu (tel que le P2P qui se servait des hôtes comme hôtes et comme serveur/relais), certains ports alors réservées à certaines fonctions ne le sont plus avec le NAT.

**À noter:** La différence entre l'adresse MAC et IP est que l'adresse IP assure l'identité de la machine sur le réseau tandis que l'adresse MAC identifie est l’adresse du périphérique en contact avec le réseau. Par analogie, l'adresse IP représente l'adresse d'une maison tandis que l'adresse MAC le nom des propriétaires.



**IPv6:** Même principe que l'IPv4 mais avec quelques nouveautés:

```{figure} img/ipv6.png
    :scale: 50 %
```

Détaillons les différents éléments:
- Traffic Class: c'est un nombre décrivant la manière dont le paquet doit être acheminé (selon la classification de traffic: fast/ low ressource consuming, ...).
- Flow Label: c'est un marquage qui permet de préciser des traitement à faire sur le paquet.
- Payload Length: taille de la charge utile du paquet en octet.
- Next Header: cela indique le prochain en-tête à mettre à la suite pour regrouper les fragments.
- Hop Limit: Correspond au Time-To-Live de l'IPv4.

**À noter** qu'en IPv6, les routeurs ne fragmentent plus eux-même le paquet, ils vont juste renvoyer un paquet ICMPv6 qui indique que le paquet est trop gros et c'est l’émetteur qui devra s'en charger.







## Routage: principe et protocoles
Chaque routeur a ce que l'on appelle une table de routage qui est une liste des adresses IP des appareils connectés a ses périphériques, le principe est que, quand ce dernier reçoit un paquet, il va comparer l'adresse IP du destinataire aux adresses de sa table et va renvoyé le paquet à la machine qui a l'adresse la plus proche (le nombre qui possède le plus de nombre en corrélation de gauche à droite).


### Les 2 types de routage
On distingue deux types de routage selon la manière de gérer les tables de routage:
- Routage statique (ou stdr): Cela consiste à modifier manuellement la table de routage, ceci est intéressant si l'on se trouve dans le cas d'un router connecté à 2-3 réseaux (nous détaillerons par la suite comment cela se fait).
- Routage dynamique: Au lieu de devoir modifier soi-même la table de routage, nous allons déléguer le boulot à des protocoles implémentés dans le routeur.



### Protocoles de routage
Un routeur possède dans son hardware un processeur que l'on appelle "processeur de route", ce dernier se décompose en 2 parties:
- Control Processor: Analyse l'intégrité des paquets.
- Forwarding paquet engine: gère la réception et redirection des paquets par les divers ports du routeurs.

Ce processeur est chargé d'appliquer les protocoles de routages (RIP, IGRP, OSPF, ...) qui assure et optimise les transfert, mais également tout les protocoles de management notamment en cas de défaillance: (ICMP, IGMP, SNMP, ...). Il existe différents protocoles chacun dédicacé à des fonctions spécifiques pour des inputs spécifiques. Néanmoins comme les paquets arrivant à un routeur peuvent être divers et variés, tout routeur doit adopter l'ensemble des protocoles existant afin d'assurer un bon fonctionnement. Ce sera pour cette raison que nous ne détaillerons pas les divers protocoles existant.




### Types de routeurs
Il existe plusieurs types de routeurs selon leurs fonctions dans le réseau.
- Routeur de coeur de réseau: Font office d’intermédiaire sur les grandes lignes (optimisent la bande passantes).
- Routeur de bordure: routeur à la frontière d'un réseau local qui reçoit/envoie les paquets.
- Routeur de distribution: reçoit des paquets IP du routeur en périphérie et les transfert par MAC aux hôtes (hybride routeur-switch/wireless access point).
- Routeur sans fil: Ce sont les routeurs domestiques par excellence qui combinent les routeurs de périphérie et celles de distribution avec le wifi.
- Routeur virtuel: ce sont des fonctions que l'on peut demander à un ordinateur de faire afin de lui faire jouer quelques aspects du routeur.




## Hardware d'un routeur
```{figure} img/router.jpg
    :scale: 50 %
```

Un routeur classique va contenir les éléments suivants:
- Controller ship: Le microprocesseur, comme sur un ordinateur, exécute des commandes (pour les fonctions de routages/ initialisation du système/...) afin de faire fonctionner le routeur.

- ROM: La mémoire morte (mémoire non volatile mais non modifiable après sa sortie d'usine) va contenir différentes instructions (pour le démarrage du routeur, pour le système d'exploitation et quelques tests)
    
- RAM: La mémoire vive va retenir les tables de routages du moment et certaines configurations (quand on l'éteint, on perd ces données).
    
- NVRAM: La mémoire vive non volatile contient la "startup-config file" qui lui donne les paramètres de démarrage pour atteindre une certaines configuration. Certains routeurs se passent de ce composant et/ou vont chercher les informations sur un serveur tftp (Trivial File Transfer Protocol) prévu à cet effet.

- Flash Memory: la mémoire flash (usb/ssd) contient tout le système d'exploitation du routeur.

- Interfaces de connexion: ce sont les ports physiques d'entrées/sorties où transitent les paquets.

- Bus: il s'agit de la liasion physique sur la carte électronique qui relie les interfaces avec le CPU. Il existe aussi des bus pour le cpu qui le relie aux systèmes de stockages de données (NVRAM/ROM/...).

- Power Supply: système d'alimentation du routeur




### Sécurité derrière les routeurs

La sécurité des routeurs touche la couche de transport des modèles vus précédemment:
- **Logiciel pare-feu (firewall)**: Il s'agit d'un logiciel souvent combiné aux routeurs domestique/ de bordure qui va faire office de barrière de sécurité entre un réseau privé et l'internet. ce dernier va trier les informations en fonctions d'une "access control list" qui va dire quel IP est valide ou non. Le problème du firewall est qu'il ne pourra pas être utilisé pour tout les cas notamment par des serveurs (les requêtes viennent de partout).
- **Au niveau du wifi:** la famille des WPA (WI-FI Protected Access) pour faire simple se sert d'un protocole sécurisé de chiffrement (TKIP/CCMP).


## Conversion d'un Raspberry Pi en routeur
L'idée de cette section va être de donner une suite d'instruction afin de se servir d'un raspberry pi en routeur. Le software d'un routeur étant trop complexe à écrire et les versions opensources étant particulièrement rares pour des raisons évidentes de sécurité, nous allons simplement voir comment installer et configurer l'application RaspAP qui va néssecité quelques lignes de commandes dans le terminal Raspian d'un Raspberry (4B dans notre cas) .
Voici les étapes clés:
- Installer sur une carte ssd 32Gb via l'application Raspberry Pi Imager le système d'exploitation "Raspberry Pi OS (32-bit)" puis toujours sur l'ordinateur, aller dans le terminal et tapez successivement les commandes suivantes (en faisant « Enter » après chaque ligne, ce principe s’appliquera pour toutes les lignes à mettre dans les terminaux):

		cd /Volumes/boot
		touch ssh 
		nano wpa_supplicant.conf

En 1 bloc:


    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=your_ISO-3166_two-letter_country_code


    network={
        ssid="my_SSID"
        psk="my_PSK"
        key_mgmt=WPA-PSK
        }

Puis modifier en fonction du wifi déjà disponible. puis appuyer sur Control+x, ensuite y, ensuite:

    cd

Et l’on peut retirer la clé ssd.

Après avoir plugger la carte dans le raspberry pi, puis avoir mis les paramètres de base, il faut ouvrir le terminal:


    ssh pi@raspberrypi.local
    yes

Le mot de passe sera **raspberry**

    sudo apt update
    sudo apt full-upgrade
    Y
    sudo reboot

Après l'avoir redémarré, revenir sur le terminal:


    ssh pi@raspberrypi.local
    raspberry
    sudo raspi-config

Cela va nous amener vers une fenêtre de configuration, il faut prendre l'item "Localisation Options" et mettre le WLAN country sur CH, ensuite revenir sur la page d'avant et sélectionner *Finish*.

    sudo reboot

Après le redémarrage, revenir sur le terminal:

    ssh pi@raspberrypi.local
    raspberry
    curl -sL https://install.raspap.com | bash

Ensuite il va configurer le software de RaspAP sur le raspberry pi, nous recommandons de répondre **Y** à ce qui est recommandé et **N** à ce qui ne l'est pas forcement. 
- Après, il faut venir sur DuckDuckGo (le moteur de recherche sur le raspberry pi) et tapper *raspberrypi.local/* et entrer l'username **admin** avec le code **secret**.
- Nous arrivons alors sur une nouvelle page, il faut sélectionner *Hotspot*, changer le SSID (le nom du raspberry qui apparaîtra lorsque l'on cherchera à s'y connecter), 
puis il nous faudra cliquer sur la colonne *Security* pour changer le mot de passe, 
enfin il faut venir à la colonne *Advanced*, mettre que l'on est en Suisse puis cliquer sur *Save settings*. 
Ensuite il nous faut revenir à la colonne *Advanced* et activer le *Wifi client AP mode* qui va assurer l'accès depuis le raspberry pi à l'internet.
Il faut cliquer sur *start hotspot*, ensuite changer le eth0 en wlan0 (si l'on veut une connexion des utilisateurs au raspberry sans fils), *save settings*
Cela indiquera que l'interface active sera l'uap0 (qui relie ce routeur à celui de la maison sans fil).
Et finalement, il suffira de se connecter au raspberry pi avec son téléphone/ordinateur.

## Source
- Designing SwitchRouters Architectures and Applications, James Aweya
- Designing SwitchRouters Fundamental Concepts and Design Methods, James Aweya
- https://labo-tech.fr/base-de-connaissance/comment-faire-un-relais-dhcp/
- https://cisco.goffinet.org/ccna/ipv4/en-tetes-ipv4-et-ipv6
- https://www.frameip.com/nat/
- https://linux-note.com/modele-osi-et-tcpip/
- https://www.geeksforgeeks.org/network-address-translation-nat/
- https://support.google.com/googlenest/answer/6274112?hl=fr
- https://www.cisco.com/c/fr_ch/solutions/small-business/resource-center/networking/what-is-a-router.html#~types-de-routeurs
- https://www.manageengine.com/fr/network-configuration-manager/configlets/what-is-nat.html
- https://www.ibm.com/docs/fr/aix/7.3?topic=routing-static-dynamic
- https://www.thewantricks.com/2019/09/the-intelligent-router-and-its.html
- https://www.youtube.com/watch?v=m2JvWFr8bX4