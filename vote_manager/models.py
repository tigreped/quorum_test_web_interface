from django.db import models

# Create your models here.

class Legislator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    primary_sponsor = models.ForeignKey(Legislator, on_delete=models.CASCADE)

class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

class VoteResult(models.Model):
    id = models.IntegerField(primary_key=True)
    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    vote_type = models.IntegerField()  # 1 for yea, 2 for nay
