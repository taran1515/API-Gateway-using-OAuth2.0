from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100, null=False,
                            help_text="This field is required")
    done = models.BooleanField(default=False)