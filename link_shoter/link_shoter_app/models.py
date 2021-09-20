from django.db import models

class Link(models.Model):
    input_link = models.CharField(max_length=255,)
    output_link = models.CharField(max_length=255, unique = True)
    date_create_link = models.DateTimeField(auto_now_add = True)
