from django.db import models
from django.contrib.auth.models import User

class Mem(models.Model):
	class Meta():
		db_table='mem'
	img=models.ImageField(upload_to='images')
	text=models.TextField(max_length=3000)
	user_ForeignKey=models.ForeignKey(User, on_delete=models.PROTECT)
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)

class User_likes_mem(models.Model):
	class Meta():
		db_table='user_likes_mem'
	user_ForeignKey=models.ForeignKey(User, on_delete=models.PROTECT)
	mem_ForeignKey=models.ForeignKey(Mem, on_delete=models.PROTECT)
	value=models.IntegerField() #1 or -1

class Mem_in_q(models.Model):
	class Meta():
		db_table='mem_in_q'
	user_ForeignKey=models.ForeignKey(User, on_delete=models.PROTECT)
	mem_ForeignKey=models.ForeignKey(Mem, on_delete=models.PROTECT)