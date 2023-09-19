from django.db import models

# Create your models here.
class CommentsTable(models.Model):
  comment = models.TextField(max_length=250)
  timestamp = models.DateTimeField(auto_now_add=True)
  likes = models.IntegerField(default=0)

class NewsFeed(models.Model):
  ticker = models.CharField(max_length=10)

class ScrollingTicker(models.Model):
  ticker = models.CharField(max_length=10)
  timestamp = models.DateTimeField(auto_now_add=True)

class chartData(models.Model):
  ticker = models.CharField(max_length=10)
  timestamp = models.DateTimeField(auto_now_add=True)
 