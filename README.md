This is version 1 of my Django Project Cheepees.

1. Create workstation, create repository and add files to github.
2. bash - sudo pip3 install Django==1.11
          django-admin startproject cheepeeWebsite .   (Project Name = cheepeeWebsite) - this will create a new folder (don't forget the .)
          python3 manage.py runserver $IP:$C9_PORT - this will generate a URL which will not work just yet.
3. The URL will load but you will get an error message - this gives you the host name which you have to copy. In this case it is django-project-v1-rory95.c9users.io
4. Open settings.py add the URL to the ALLOWED_HOSTS line, for example ALLOWED_HOSTS = ['django-project-v1-rory95.c9users.io']
5. Refresh the URL it should now not return an error.
6. Stop the server running with CTRL C
7. Open the .bash-aliases file and add the following at the bottom... alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT"
8. Type Exit on the bash terminal, then open a new one and type the command 'run' - then check the URL is still working. 

9. 