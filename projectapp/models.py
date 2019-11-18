
from django.db import models


class Label(models.Model):
    label_name = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.label_name


class Language(models.Model):
    repo_language = models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.repo_language


class Repositories(models.Model):
    repo_address = models.CharField(max_length=80, null=False)
    repository_label = models.ManyToManyField(Label)
    repository_language = models.ManyToManyField(Language)

    def __str__(self):
        return  self.repo_address

