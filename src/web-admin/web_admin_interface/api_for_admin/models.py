from django.db import models

# Create your models here.
class Tokens(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='owner', blank=True, null=True)
    value_hash = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokens'


class Users(models.Model):
    username = models.TextField(primary_key=True)
    password_hash = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'