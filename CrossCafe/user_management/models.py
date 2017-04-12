from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''Extending the User class'''
    USER_TYPE = [('customer', 'Customer'), ('manager', 'Manager'), ('attendant', 'Attendant'), ('delivery_boy', 'Delivery Boy'), ('chef', 'Chef')]
    ACC_STATUS = [('active', 'Active'), ('verified', 'Verified'), ('blacklisted', 'Blacklisted')]
    user = models.ForeignKey(User, to_field = 'id')
    user_type = models.CharField(max_length=30, choices=USER_TYPE, default=USER_TYPE[0])
    user_email = models.EmailField(max_length=70, blank=True, null= True, unique= True)
    user_phone = models.CharField(max_length = 15, blank=True, null= True)
    user_name = models.CharField(max_length = 50)
    activation_key = models.CharField(max_length = 257)
    key_expires = models.DateTimeField()
    acc_status = models.CharField(max_length=30, choices=ACC_STATUS, default=ACC_STATUS[0])

    def __str__(self):
        return '%s, %s' % (self.user.id, self.user.username)
