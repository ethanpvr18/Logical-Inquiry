from django.db import models

class LineItem(models.Model):
    line_number = models.CharField(max_length=255, default="")
    formula = models.CharField(max_length=255, default="")
    justification = models.CharField(max_length=255, default="")
    assumption_dependence = models.CharField(max_length=255, default="")