from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    code = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)