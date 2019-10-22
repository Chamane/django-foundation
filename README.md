# Django Foundation
Un puissant kit de démarrage

## Fonctionnalités
  * Bootstrap 4 integré
  * Authentification déja implémentée Login/Register
  * Implémentation des [12 facteurs](https://12factor.net)
  * Fonctionne avec Python 3 et Django 2
  * Bases de données PostgreSQL
  * Respecte les bonnes pratique du livre [Two Scoops of Django](https://twoscoopspress.com/products/two-scoops-of-django-1-11)
  * Tests unitaires
  * DevOps avec [Fabric](http://www.fabfile.org/)

## Démarrage rapide (Quick Start)

  1. Installer [Python 3](https://www.python.org/downloads/) et PIP
    normalement sur Linux Python est présent par défaut. [Tutoriel sur
    comment installer pip sur windows](https://www.liquidweb.com/kb/install-pip-windows/)

  2. Une fois Python 3 et pip installé il vous faut avoir un outil pour créer des
    environnements python isolés. Nous allons utiliser virtualenv et virtualenwrapper.

      Ouvrez votre terminal et executez ces commandes:

        ```
        pip install virtualenv
        ```
      Une fois virtualenv installé, vous devez installer virtualenvwrapper, si vous
      êtes sur Linux la commande est:

        ```
        pip install virtualenvwrapper
        ```
      si vous êtes sur windows vous devez saisir:

      	```
        pip install virtualenwrapper-win
        ```
  3. Cloner le repo de django-foundation sur votre ordinateur.

     > l'outil git est requis

     ```
     git clone https://github.com/chamane/django-foundation
     ```

  4. Configurez un environnement isolé python pour travailler

      Ouvrez le terminal sur votre ordinateur et saisissez:

      ```
      mkvirtualenv myEnv
      ```

  5. Installez les dépendances de django-foundation.

      Ouvrez le terminal et déplacez vous dans le répertoire de django-foundation
      sur votre ordinateur. Ensuite placez vous dans l'environnement créé plutôt grace a ceci:
      ```
      workon myEnv
      ```

      et maintenant vous pouvez installer les dépendances du projet qui se trouve déja
      dans les requirements.

      ```
      pip install -r requirements-dev.txt
      ```
   6. Installez PostgreSQL sur votre ordinateur. 
