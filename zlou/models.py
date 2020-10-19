import datetime

from django.db import models



class Keys(models.Model):
    keys = models.CharField(max_length=50)
    keys_date = models.DateTimeField('date published')
    class Meta:
        #managed = False
        db_table = 'Keys'
    def __str__(self):
        return self.keys

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
