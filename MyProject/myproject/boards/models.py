from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add= True)
    board = models.ForeignKey(Board, on_delete = models.CASCADE, related_name= 'topics')
    starter = models.ForeignKey(User,on_delete = models.CASCADE, related_name='topics')

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null = True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, related_name='+')

#The User model is already defined inside a built-in app named auth which is listed in our INSTALLED_APPS configuration under the namespace django.contrib.auth
#The virtual environment as to be first activated from the directory where venv resides with the help of the command "venv\Scripts\activate"
#then move to the directory where manage.py resides and migrate the models using the command "python manage.py makemigrations"
#to find the above model code which is translated into SQL, run "python manage.py sqlmigrate boards 0001"
#the next step is applying the migrations using the command "python manage.py migrate"
#we can get an interactive shell with the command "python manage.py shell"
'''
from boards.models import Board
boards_list = Board.objects.all() #this is a query set, but visible due to __str__ method
for board in boards_list:
    print(board.description)
'''

'''
#Every Django model comes with a special attribute; we call it a Model Manager. You can access it via the Python attribute 'objects'. It is used mainly to execute
queries in the database. we could use it to directly create a new board object
board = Board.objects.create(name='',description='')
Board.objects.get(id = 1) #getting the objects based on the id
'''
