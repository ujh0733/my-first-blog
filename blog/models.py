from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)	#다른모델 링크
	title = models.CharField(max_length=200)		#글자수제한
	text = models.TextField()						#제한이 없는 긴 텍스트
	create_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text