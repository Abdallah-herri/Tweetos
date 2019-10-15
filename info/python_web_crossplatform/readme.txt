1] mettre le .htaccess (qui est dans ce dossier) a la racine de votre répertoire web

2] vous devez suivre les étapes suivante uniquement si vous êtes sur windows

3] ouvrir httpd.conf
4] ajouter à la fin du fichier :
ScriptInterpreterSource Registry-Strict

5] lancer le fichier win_shebang.reg

6] redémarrer le serveur
