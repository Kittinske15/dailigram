from django.db import models
from django.urls import reverse
import datetime


class Diary(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    # is_favorite = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('diary:index')


class Tag(models.Model):
    name = models.CharField(
        max_length=200, help_text='Enter a tag (e.g. Love, Happy, Sad)')

    def __str__(self):
        return self.name


class Page(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    story = models.TextField(max_length=10000, help_text='Write your story.')
    date = models.CharField(max_length=50, blank=True)
    picture = models.FileField()

    def __str__(self):
        return f'{str(self.date)}, {self.diary}, {self.tag}'

    def get_absolute_url(self):
        return reverse('diary:index')
