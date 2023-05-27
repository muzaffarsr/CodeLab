from django.shortcuts import render
from .models import Article, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
	articles = Article.objects.order_by('-pub_date')
	context = {
		'articles':articles,
	}
	return render(request, 'main/index.html', context)


def search(request):
	articles = Article.objects.filter( title__icontains = request.GET.get('search') ).order_by('-pub_date')
	context = {
		'articles':articles,
	}
	return render(request, 'main/index.html', context)


def article(request, aid):
	article = Article.objects.get( id = aid )
	comments = Comment.objects.filter( article = aid ).order_by('-pub_date')
	context = {
		'article':article,
		'comments':comments,
	}
	return render(request, 'main/article.html', context)


def comment(request, aid):
	article = Article.objects.get( id = aid )
	article.comment_set.create( author = request.POST['author'], text = request.POST['text'] )
	return HttpResponseRedirect( reverse('article', args = {article.id,}) )