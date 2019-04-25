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

9. bash - django-admin startapp cheepeeApp - check that the folder and files have been created.
10. Add new folder under the app folder by rightclicking, call it folder. 
11. Create a html file within this - in this instance I created allCheepees.html - check it has been created.
12. Open urls.py and add a function:
 
                                        def get_allCheepees(request):
                                            return render(request, "allCheepees.html")

13. Open urls.py and add the following line to the import section - from cheepeeApp.views import get_allCheepees.html
14. in urls.py add the following line to the urlpatterns section - url(r'^$', get_allCheepees)
15. Open the settings.py file and add the appname to the end of the installed apps list e.g cheepeeApp
16. Test that the page is working by stopping the server (CTRL C) and starting it again with the run command. 

17. bash - python3 manage.py migrate - this wil run the python setup migrations
18. Go into sqlite3 by pressing (CTRL C) followed by - sqlite3 db.sqlite3 - then check tables exist by typing .tables, then type .quit to exit.
19. Create super user - bash - python3 manage.py createsuperuser - then fill in your details.
20. Test that the admin pages are working correctly by going to the base url and adding /admin to the end. Try and sign in. 
21. Click on the Cog and check "Show home in favourites" and "Show Hidden Files"
22. Create a new file in the root (~) folder called .sqliterc







..... Create the static folder with another subfolder called css
..... Add the following code to the settings.py file 
STATICFILES_DIRS = [
	"/django-project-v1/cheepeeApp/static",
]