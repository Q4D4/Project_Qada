from django.db import models
# FileSystemStorage
from django.core.files.storage import FileSystemStorage
# Settings
from django.conf import settings
# Signals
from django.db.models.signals import post_save, post_delete
# Pillow
from PIL import Image
# OS
import os


static_storage = FileSystemStorage(location=settings.BASE_DIR + '/portfolio/static/portfolio/')



class Language(models.Model):
	lang_name			= models.CharField(max_length=200)


	class Meta:
		db_table 		= 'language'


	def __str__(self):
		return self.lang_name


class About(models.Model):
	first_name			= models.CharField(max_length=50)
	last_name			= models.CharField(max_length=50)
	birth_date			= models.DateField()
	short_bio			= models.TextField(max_length=300)
	country				= models.CharField(max_length=100)
	city				= models.CharField(max_length=100)
	phone				= models.CharField(max_length=50, blank=True, null=True)
	email 				= models.EmailField(max_length=1000, null=True, blank=True)
	nationality			= models.CharField(max_length=100, default='Georgian')
	languages			= models.ManyToManyField(Language)
	experience_years	= models.IntegerField(default=0)
	completed_projects	= models.IntegerField(default=0)
	happy_clients		= models.IntegerField(default=0)
	awards_won			= models.IntegerField(default=0)
	facebook_profile	= models.CharField(max_length=1000, blank=True, null=True)
	instagram_profile	= models.CharField(max_length=1000, blank=True, null=True)
	twitter_profile		= models.CharField(max_length=1000, blank=True, null=True)
	github_profile		= models.CharField(max_length=1000, blank=True, null=True)
	profile_image		= models.ImageField(storage=static_storage)


	class Meta:
		db_table		= 'about'


	def __str__(self):
		return str(self.first_name) + ' ' + str(self.last_name)


class Skill(models.Model):
	skill_name			= models.CharField(max_length=50)
	image				= models.ImageField(storage=static_storage)


	class Meta:
		db_table		= 'skill'


	def __str__(self):
		return self.skill_name


class Feedback(models.Model):
	name 				= models.CharField(max_length=100)
	email 				= models.EmailField(max_length=100)
	subject 			= models.CharField(max_length=100)
	message				= models.TextField(max_length=500)
	date_time			= models.DateTimeField(auto_now_add=True)


	class Meta:
		db_table		= 'feedback'


	def __str__(self):
		return str(self.name) + ' | ' + str(self.date_time)


class Category(models.Model):
	category_name 		= models.CharField(max_length=50)


	class Meta:
		db_table		= 'category'


	def __str__(self):
		return self.category_name


class Project(models.Model):
	project_name 		= models.CharField(max_length=50)
	used_technologies 	= models.ManyToManyField(Skill)
	categories			= models.ManyToManyField(Category)
	repository_link 	= models.CharField(max_length=10000, null=True, blank=True)
	link_to_project 	= models.CharField(max_length=10000, null=True, blank=True)
	about_project		= models.TextField(max_length=500, null=True, blank=True)
	photo				= models.ImageField(storage=static_storage)


	class Meta:
		db_table 		= 'project'


	def __str__(self):
		return self.project_name


# SIGNALS
def about_save(sender, instance, *args, **kwargs):
	try:
		image 			= Image.open(instance.profile_image)
		path			= settings.BASE_DIR + '/portfolio/static/portfolio/profile-images/'

		# HIGH
		(width, height) = (int(image.width // 1.5), int(image.height // 1.5))
		resized_high	= image.resize((width, height), Image.ANTIALIAS)
		resized_high.save(path + str(instance.id) + '_high.jpg', format='JPEG')

		# MEDIUM
		(width, height) = (int(image.width // 2), int(image.height // 2))
		resized_medium	= image.resize((width, height), Image.ANTIALIAS)
		resized_medium.save(path + str(instance.id) + '_medium.jpg', format='JPEG', quality=70)

		# LOW
		(width, height) = (int(image.width // 3), int(image.height // 3))
		resized_low		= image.resize((width, height), Image.ANTIALIAS)
		resized_low.save(path + str(instance.id) + '_low.jpg', format='JPEG', quality=70)

		# REMOVE ORIGINAL
		os.remove(instance.profile_image.path)
	except:
		pass


def about_delete(sender, instance, *args, **kwargs):
	path				= settings.BASE_DIR + '/portfolio/static/portfolio/profile-images/'

	# REMOVE HIGH
	try:
		os.remove(path + str(instance.id) + '_high.jpg')
	except:
		pass

	# REMOVE MEDIUM
	try:
		os.remove(path + str(instance.id) + '_medium.jpg')
	except:
		pass

	# REMOVE LOW
	try:
		os.remove(path + str(instance.id) + '_low.jpg')
	except:
		pass


def project_save(sender, instance, *args, **kwargs):
	try:
		image			= Image.open(instance.photo)
		path			= settings.BASE_DIR + '/portfolio/static/portfolio/project-images/'

		# HIGH
		(width, height) = (int(image.width // 1.5), int(image.height // 1.5))
		resized_high	= image.resize((width, height), Image.ANTIALIAS)
		resized_high.save(path + str(instance.id) + '_high.jpg', format='JPEG')

		# MEDIUM
		(width, height) = (int(image.width // 2), int(image.height // 2))
		resized_medium	= image.resize((width, height), Image.ANTIALIAS)
		resized_medium.save(path + str(instance.id) + '_medium.jpg', format='JPEG', quality=70)

		# LOW
		(width, height) = (int(image.width // 3), int(image.height // 3))
		resized_low		= image.resize((width, height), Image.ANTIALIAS)
		resized_low.save(path + str(instance.id) + '_low.jpg', format='JPEG', quality=70)

		# REMOVE ORIGINAL
		os.remove(instance.photo.path)
	except:
		pass


def project_delete(sender, instance, *args, **kwargs):
	path				= settings.BASE_DIR + '/portfolio/static/portfolio/project-images/'

	# REMOVE HIGH
	try:
		os.remove(path + str(instance.id) + '_high.jpg')
	except:
		pass

	# REMOVE MEDIUM
	try:
		os.remove(path + str(instance.id) + '_medium.jpg')
	except:
		pass

	# REMOVE LOW
	try:
		os.remove(path + str(instance.id) + '_low.jpg')
	except:
		pass


def skill_save(sender, instance, *args, **kwargs):
	try:
		image			= Image.open(instance.image)
		path			= settings.BASE_DIR + '/portfolio/static/portfolio/skill-images/'

		# HIGH
		(width, height) = (int(image.width // 1.5), int(image.height // 1.5))
		resized_high	= image.resize((width, height), Image.ANTIALIAS)
		resized_high.save(path + (instance.skill_name).strip().replace(' ', '_') + '_high.png', format='PNG')

		# MEDIUM
		(width, height) = (int(image.width // 2), int(image.height // 2))
		resized_medium	= image.resize((width, height), Image.ANTIALIAS)
		resized_medium.save(path + (instance.skill_name).strip().replace(' ', '_') + '_medium.png', format='PNG')

		# LOW
		(width, height) = (int(image.width // 3), int(image.height // 3))
		resized_low		= image.resize((width, height), Image.ANTIALIAS)
		resized_low.save(path + (instance.skill_name).strip().replace(' ', '_') + '_low.png', format='PNG')

		# REMOVE ORIGINAL
		os.remove(instance.image.path)
	except:
		pass


def skill_delete(sender, instance, *args, **kwargs):
	path				= settings.BASE_DIR + '/portfolio/static/portfolio/skill-images/'

	# REMOVE HIGH
	try:
		os.remove(path + (instance.skill_name).strip().replace(' ', '_') + '_high.png')
	except:
		pass

	# REMOVE MEDIUM
	try:
		os.remove(path + (instance.skill_name).strip().replace(' ', '_') + '_medium.png')
	except:
		pass

	# REMOVE LOW
	try:
		os.remove(path + (instance.skill_name).strip().replace(' ', '_') + '_low.png')
	except:
		pass


post_save.connect(about_save, sender=About)
post_delete.connect(about_delete, sender=About)
post_save.connect(project_save, sender=Project)
post_delete.connect(project_delete, sender=Project)
post_save.connect(skill_save, sender=Skill)
post_delete.connect(skill_delete, sender=Skill)