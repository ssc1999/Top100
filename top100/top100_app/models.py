from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 13)
    mail = models.CharField(max_length = 100)
    message = models.CharField(max_length = 2000)

    def __str__(self):
        return self.mail

class Gender(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return "Author: " + self.name

class Song(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    gender = models.ManyToManyField(Gender)
    repros = models.IntegerField()

    def __str__(self):
        return "Song: " + self.name

class Album(models.Model):
    name = models.CharField(max_length = 20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    gender = models.ManyToManyField(Gender)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    repros = models.IntegerField()

    def __str__(self):
        return "Album: " + self.name



