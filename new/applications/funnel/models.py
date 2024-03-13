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

    class Meta:
        db_table = 'Leads from a paid funnel'


class LeadCourse(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    courseid = models.CharField(max_length=60, default='')
    course_name = models.CharField(max_length=100, default='')
    first_cost = models.CharField(max_length=15, default='')
    second_cost = models.CharField(max_length=15, default='')
    start = models.CharField(max_length=20, default='')
    open_date_bool = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.lead
