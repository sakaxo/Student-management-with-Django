from django.db import models



class Student(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.fname + " " + self.lname
