from django.db import models
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Mem(models.Model):
	class Meta():
		db_table='mem'
	img=models.ImageField(upload_to='images')
	text=models.TextField(max_length=3000,blank=True)
	user_ForeignKey=models.ForeignKey(User, on_delete=models.PROTECT)
	likes=models.IntegerField(default=0)
	dislikes=models.IntegerField(default=0)
	date = models.DateTimeField(auto_now=True)

	# def save(self):
	# 	#Opening the uploaded image
	# 	im = Image.open(self.img)

	# 	output = BytesIO()

	# 	#Resize/modify the image
	# 	size = (400,400)
	# 	im.thumbnail(size, Image.ANTIALIAS)
	# 	background = Image.new('RGBA', size, (255, 255, 255, 0))
	# 	background.paste(
	# 		im, (int((size[0] - im.size[0]) / 2), int((size[1] - im.size[1]) / 2))
	# 	)
	# 	im = background.convert('RGB')

	# 	#after modifications, save it to the output
	# 	im.save(output, format='JPEG', quality=100)
	# 	output.seek(0)
	# 	#change the imagefield value to be the newley modifed image value
	# 	self.img = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.img.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
	# 	super(Mem,self).save()

class User_likes_mem(models.Model):
	class Meta():
		db_table='user_likes_mem'
	user_ForeignKey=models.ForeignKey(User, on_delete=models.PROTECT)
	mem_ForeignKey=models.ForeignKey(Mem, on_delete=models.PROTECT)
	value=models.IntegerField() #1 or -1
	date = models.DateTimeField(auto_now=True)

class Mem_in_q(models.Model):
	class Meta():
		db_table='mem_in_q'
	user_ForeignKey=models.ForeignKey(User, on_delete=models.PROTECT)
	mem_ForeignKey=models.ForeignKey(Mem, on_delete=models.PROTECT)