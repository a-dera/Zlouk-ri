import datetime

from django.db import models



class Words(models.Model):
    words = models.CharField(max_length=50)
    words_date = models.DateTimeField('date published')
    #class Meta:
        #managed = False
        #db_table = 'Keys'
    def __str__(self):
        return self.words

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
