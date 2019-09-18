import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    def was_published_recently(self):
        return self.pub_date >= timezoncreae.now() - datetime.timedelta(days=1)