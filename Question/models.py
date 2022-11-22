from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    explanation = models.CharField(max_length=300, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


    def __str__(self):
        return self.question
