from django.db import models


class LeadCourse(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    courseid = models.CharField(max_length=60, default='')
    course_name = models.CharField(max_length=100, default='')
    first_cost = models.CharField(max_length=15, default='')
    second_cost = models.CharField(max_length=15, default='')
    start = models.CharField(max_length=20, default='')
    open_date = models.BooleanField(max_length=20, default=False)
    non_existent_course = models.BooleanField(default=False)

    def __str__(self):
        return self.lead

    class Meta:
        db_table = "Lead's Course"
