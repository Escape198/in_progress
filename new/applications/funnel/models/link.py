import datetime
from django.db import models
from new.settings import ALLOWED_HOSTS


class Link(models.Model):
    lead = models.ForeignKey('LeadCourse', on_delete=models.CASCADE)
    time = models.CharField(max_length=60, default='')
    deal_id = models.CharField(max_length=100, default='')
    link = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.link

    def idtp_generate(self, now, course):
        self.time = datetime.datetime.now()
        unix_timestamp = self.to_unixtime(self.time)
        self.generate_deal_id(course.courseid, unix_timestamp)
        self.create_link(course.first_cost)
        self.lead = course

        self.save()

    def to_unixtime(self, time):
        return str(int(datetime.datetime.timestamp(self.time)*1000000))

    def generate_deal_id(self, courseid, unix_timestamp):
        self.deal_id = f'X-{courseid}-{unix_timestamp}'

    def create_link(self, first_cost):
        self.link = f'{ALLOWED_HOSTS[0]}/' \
            f'order/{self.deal_id}?count={first_cost}'

    class Meta:
        db_table = "Links"
