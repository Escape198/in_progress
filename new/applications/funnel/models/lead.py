from django.db import models


class Lead(models.Model):
    time = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=70, default='')
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=30, default='')

    courseid = models.CharField(max_length=50, default='')
    deal_idtp = models.CharField(max_length=60, default='')
    link = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.deal_idtp

    def check_required_fields(self, *args):
        return all(*args) 

    def setattr_request(self, post: dict) -> None:
        for key in post:
            setattr(self, key, post[key])
        self.save()

    class Meta:
        db_table = 'Leads from a paid funnel'
