from django.db import models


class Article(models.Model):
	preview = models.TextField('Article Preview Image Link')
	img = models.TextField('Article Image Link', blank=True)
	title = models.TextField('Article Title')
	text = models.TextField('Article Text')
	youtube_link = models.TextField('Article Youtube Video Link', blank=True)
	pub_date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.text
	def __str__(self):
		return self.title


class Comment(models.Model):
	author = models.CharField('Comment Author', max_length = 50)
	text = models.TextField('Comment Text')
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	pub_date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.author
	def __str__(self):
		return self.text