import datetime

from django.db import models


class Lead(models.Model):
    time = models.CharField(max_length=30, default='')

    name = models.CharField(max_length=70, default='')
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=30, default='')

    request_cookie = models.TextField(default='')
    request = models.TextField(default='')
    courseid = models.CharField(max_length=50, default='')
    courseid_string = models.CharField(max_length=50, default='')
    form_id = models.CharField(max_length=80, default='')
    deal_idtp = models.CharField(max_length=60, default='')
    type_pay = models.CharField(max_length=60, default='')
    link = models.CharField(max_length=150, default='')
    privacy = models.CharField(max_length=5, default='')
    distribution = models.CharField(max_length=5, default='')

    def __str__(self):
        return self.deal_idtp

    def check_required_fields(self, *args):
        return all(*args)

    def setattr_request(self, post: dict) -> None:
        for key in post:
            setattr(self, key, post[key])
        self.set_courseid()

    def set_courseid(self):
        self.courseid_str = ''.join((
            x for x in self.courseid if not x.isdigit())).lower()
        self.courseid = self.courseid.lower()
        self.time = datetime.datetime.now()
        self.save()

    class Meta:
        db_table = 'Leads from a paid funnel'
