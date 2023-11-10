TP : Processus et système d'exploitation linux
==============================================

**GNU/Linux** est un système d'exploitation créé par Richard Stallman et Linus Thorvald dans les années 1990. Comme windows, il s'installe sur les ordinateurs de type PC et propose les mêmes services et applications.

Ce système d'exploitation peut être utilisé sans aucune interface graphique ce qui en fait sa force. L'utilisation de GNU/Linux se fait alors en ligne de commandes.

.. note::
   
   Ce TP se réalise sur une machine virtuelle avec le système d'exploitation **Ubuntu**. Les identifiants de connexion de cette machine virtuelle sont:

   - identifiant : nsi
   - mot de passe : Nsi2024!


Le terminal linux
-----------------

Le **terminal** ou **console** est une application qui permet de saisir ces lignes de commandes.

#. Quelles sont les commandes linux qui permettent:

   -  de lister le contenu d'un dossier :
   -  de changer de dossier :
   -  de créer un nouveau dossier :
   -  de déplacer un fichier dans un autre dossier :

#. Ouvrir une nouvelle fenêtre de "Terminal". Dans quel dossier de l'arborescence êtes-vous ?
#. Déplacez-vous dans le dossier ``Documents`` puis créer un dossier ``python``.
#. Télécharger le fichier ``pgm.py`` disponible sur l'ENT. Ce fichier est dans le cours sur les processus sur Moodle. 
#. Déplacer, en ligne de commandes, ce fichier vers le dossier ``python``.
#. Exécuter ce programme en saisissant la commande :

   .. code-block::

      nsi$: ./pgm.py

   Le code s'est-il exécuté correctement ?
   
#. Si un problème de permissions a empêché l'exécution du code, il faut les modifier sur le fichier ``pgm.py``

   a. Afficher les permissions de votre fichier ``pgm.py``.
   b. Si vous remarquez l'absence de la permission ``x`` pour l'utilisateur propriétaire ``u``, il faut l'ajouter avec la commande:

   .. code-block::

      nsi$: chmod u+x pgm.py

Les processus sous linux
------------------------

La commande ``ps`` affiche les processus utilisateur liés à la console.

Avec certaines options, la commande renvoie des informations plus ciblées. Par exemple:

-  l'option ``-f`` affiche plus d'informations sur les processus liés au terminal (console).
-  l'option ``-u`` suivi du nom utilisateur affiche les processus de l'utilisateur.
-  l'option ``-e`` affiche tous les processus de tous les utilisateurs.
-  l'option ``-o`` suivi d’arguments affiche les informations pour chaque processus et pour chaque argument passé en paramètres.

#. Afficher les processus utilisateur avec la commande ``ps`` puis avec la commande ``ps -f``.
#. Afficher les processus utilisateur avec la commande ``ps -u`` suivi du nom utilisateur.
#. Reprendre la commande précédente en y ajoutant l'option ``-f`` pour avoir plus d’informations.
#. Afficher les processus utilisateur avec les arguments pid, ppid et command.

La gestion des processus
------------------------
#. Exécuter votre programme ``pgm.py`` et afficher les processus de l'utilisateur. Le programme python figure-t-il dans la liste des processus ? Pourquoi ?
#. On peut lancer un programme en arrière-plan en ajoutant ``&`` à la fin de la commande.

   a. Exécuter votre programme ``pgm.py`` en arrière-plan.
   b. Le processus lié au programme est il affiché ? Les PID et PPID correspondent-ils ?

#. Lancer un navigateur et observer dans les processus sa présence.
   
   a. Combien de processus enfants ont été créés ?
   b. Quel est le PID et PPID du processus parent du navigateur ?

#. Il est possible de terminer (tuer) un processus avec la commande ``kill`` suivi du numéro de processus.

   Mettre fin en ligne de commande au processus associé à votre navigateur web.

#. a. Modifier votre programme ``pgm.py`` en remplaçant l'instruction ``sleep`` par une boucle infinie:

      .. code-block:: python

         while True:
            pass

   b. Exécuter votre programme ``pgm.py``. Quelles sont les différentes manières de l'arrêter ?
