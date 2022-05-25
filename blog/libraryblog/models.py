from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATUS = ((0, "Draft"), (1, "Publish"))

class Post(models.Model):
	post_title = models.CharField('Заголовок',max_length=25)
	post_img = models.ImageField('Фото поста')
	post_text = models.CharField('Підзаголовок',max_length=50)
	content = models.TextField()
	post_data = models.DateField('Дата публікації')
	post_author = models.CharField('Автор',max_length=15)
	updated_on = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=200, unique=True)
	status = models.IntegerField(choices=STATUS, default=0)


	class Meta: 
		ordering = ["-created_on"]

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse("post_detail", kwargs={"slug": str(self.slug)})

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	name = models.CharField('Ім*я', max_length=25)
	email = models.EmailField('Електронна скринька')
	body = models.TextField('Коментар')
	created_on = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ["created_on"]

	def __str__(self):
		return "Comment {} by {}".format(self.body, self.name)
		