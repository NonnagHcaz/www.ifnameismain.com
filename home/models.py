from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    primary = models.CharField(max_length=255)
    secondary = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    stars = models.IntegerField(null=True)

    def __str__(self):
        return (
            '\n\t'.join([
                '<Theme Object>',
                'Name: ' + self.name,
                'ID: ' + self.key,
                'Primary: ' + self.primary,
                'Secondary: ' + self.secondary,
                'Stars: ' + str(self.stars or 0)]))
