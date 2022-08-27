# English Instructions

# LITReview: Minimum viable product for a django based application

LITReview is a django application that has to be executed locally for demonstration purpose.
It allow testing of the functionalities required to be developped in the context of openclassroom python programmer formation.
With it, you can test the authentication system, the user following system, the ticket&review system. Its front end has been kept simple and minimal as it is a MVP.
It has been developped based on specification provided by OpenClassRoom that you can find here (In french) : https://docs.google.com/document/d/1EKfMYxuC7qFjuqUivP14HVO4_0O_DDbEifvEsoEbfBI/edit

## Installation

This locally-executable django application can be executed from [http://localhost:8000/home](http://localhost:8000/home) using the following steps.

### Installation and execution with pipenv

For this method, it is necessary to have pipenv already installed on your python installation. If pipenv is not already installed on your computer, refer to [this page](docs/pipenv/installation-en.md).

1. Clone this repository using `$ git clone https://github.com/Yohz78/Projet_9`
2. Move to the project root folder with `$ cd Projet_9\LITReview`
3. Install project dependencies with `pipenv install`
4. Run the server with `python manage.py runserver`

When the server is running after step 4 of the procedure, you can access the app at [http://localhost:8000/home](http://localhost:8000/home)

Steps 1-4 are only required for initial installation. For subsequent launches
of the application, you only have to execute step 4 from the root folder of the project.

### Option 2: Installation and execution without pipenv (using venv and pip)

1. Clone this repository using `$ git clone https://github.com/Yohz78/Projet_9`
2. Move to the LITReview root folder with `$ cd Projet_9\LITReview`
3. Create a virtual environment for the project with `$ py -m venv env` on windows or `$ python3 -m venv env` on macos or linux.
4. Activate the virtual environment with `$ env\Scripts\activate` on windows or `$ source env/bin/activate` on macos or linux.
5. Install project dependencies with `$ pip install -r requirements.txt`
6. Run the server with `$ python manage.py runserver`

When the server is running after step of the procedure, the django app can be accessed at [http://localhost:8000/home](http://localhost:8000/home)

Steps 1-5 are only required for initial installation. For subsequent launches of the Django app, you only have to execute step 6 from the root folder of the project.

## Usage

For demonstration purpose, a database has been joined to the repository. You can log as a user, create a user, follow and unfollow other user. You can ask for and post reviews. A personal publication page is also available.

You can log as the current superuser as :
Username : Admin
Email : admin@admin.fr
Password : Helloworld1

Several users have been created for demonstration purposed.
Username : TestX
Email : textX@test.fr
Password : Helloworld1

Where X is a value between 1 and 5.

# Notice d'utilisation française

# LITReview: Application django de gestion de critiques d'objets.

LITReview est une application django à des fins de démonstration devant être exécutée localement .
Elle permet de tester les fonctionnalités à développer dans le cadre de la formation de programmeur python openclassroom.
Avec ce MVP, vous pouvez tester le système d'authentification, le système de suivi des utilisateurs, le système de ticket et de revues. Son front-end est simple et minimal car il s'agit d'un MVP (Minimum Viable Product).
elle a été développée sur la base des spécifications fournies ici : https://docs.google.com/document/d/1EKfMYxuC7qFjuqUivP14HVO4_0O_DDbEifvEsoEbfBI/edit

## Installation

Cette application django exécutable localement peut être exécutée à partir de [http://localhost:8000/home](http://localhost:8000/home) en procédant comme suit.

### Installation et exécution de l'application avec pipenv

Pour cette méthode, il est nécessaire que pipenv soit déjà installé sur votre installation python. Si pipenv n'est pas déjà installé sur votre ordinateur, consultez [cette page](docs/pipenv/installation-en.md).

1. Cloner ce dépôt en utilisant `$ git clone https://github.com/Yohz78/Projet_9`
2. Accédez au dossier racine du projet avec `$ cd Projet_9\LITReview`
3. Installez les dépendances du projet avec `pipenv install`
4. Exécutez le serveur avec `python manage.py runserver`

Lorsque le serveur est en cours d'exécution après l'étape 4 de la procédure, vous pouvez accéder à l'application à l'adresse [http://localhost:8000/home](http://localhost:8000/home)

Les étapes 1 à 3 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs
de l'application, vous n'avez qu'à exécuter l'étape 4 depuis le dossier racine du projet.

### Option 2: Installation and execution without pipenv (using venv and pip)

1. Clonez le repertoire avec la commande : `$ git clone https://github.com/Yohz78/Projet_9`
2. Accédez au dossier racine du projet avec : `$ cd Projet_9\LITReview`
3. Créez l'environnement virtuel du projet avec `$ py -m venv env` sur windows ou `$ python3 -m venv env` sur macos ou linux.
4. Activez l'environnement avec `$ env\Scripts\activate` sur windows ou `$ source env/bin/activate` sur macos ou linux.
5. Installez les librairies nécessaires au projet avec `$ pip install -r requirements.txt`
6. Exécutez le serveur avec `$ python manage.py runserver`

Lorsque le serveur est en cours d'exécution après l'étape 4 de la procédure, vous pouvez accéder à l'application à l'adresse [http://localhost:8000/home](http://localhost:8000/home)

Les étapes 1 à 5 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs
de l'application, vous n'avez qu'à exécuter l'étape 6 depuis le dossier racine du projet.

## Usage

Une base de données a été jointe a fin de démonstration. Vous pouvez vous connecter en tant qu'utilisateur, créer un utilisateur, suivre et ne plus suivre un autre utilisateur. Vous pouvez demander et publier des avis. Une page personnelle est disponible.

Vous pouvez vous connecter en tant qu'admin avec les informations suivantes :
Username : Admin
Email : admin@admin.fr
Mot de passe : Helloworld1

D'autres utilisateurs ont été créés à fin de démonstration :
Username : TestX
Password : Helloworld1

X étant une valeur entre 1 et 5 (5 utilisateurs test ont été créés)
