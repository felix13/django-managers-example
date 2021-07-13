from django.db import models

class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role='A')

    def editors(self):
        return self.filter(role='E')


class Person(models.Model):

    ROLES = (

       ('A',   'Author' ),
       ('E',   'Editor' ),

     )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=ROLES, default="A" )
    people = PersonQuerySet.as_manager()
    
    
    def __str__(self):
        return self.first_name

