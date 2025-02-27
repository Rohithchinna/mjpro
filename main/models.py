from django.db import models
from .globals import uservar
from django.core.cache import cache
import json  #for networks list

# Create your models here.


class Users(models.Model):
    email=models.EmailField()
    ph_no=models.IntegerField()
    password=models.CharField(max_length=128)

    def __str__(self):
        return self.email
    



class Networks(models.Model):
    current_user=models.EmailField()
    network_users = models.TextField(default='[]')  # Initialize with an empty JSON array

    def add_item(self, network_users):
        # Load the current items
        current_items = self.get_items()
        # Add the new item
        current_items.append(network_users)
        # Save the updated list back to the items field
        self.network_users = json.dumps(current_items)
        self.save()  # Save the model instance to the database

    def get_items(self):
        return json.loads(self.network_users)
