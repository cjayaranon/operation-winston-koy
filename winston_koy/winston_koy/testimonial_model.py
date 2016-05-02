from django.db import models

"""models for testimonials"""


class Testimonial(models.Model):

    name = models.CharField(maxlength = 30)
    age = models.IntegerFields(maxlength = 2)
    user_description = models.TextField(maxlength = 50)
    pub_date = models.DateField()
    pic = models.ImageField(upload_to = '/../static/images/testimonials')
    testimony = models.TextField(maxlength = 120)
