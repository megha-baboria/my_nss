
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import post_form
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from django.utils import timezone
import json

def post_create(request):
	if request.method=='POST':
		body = request.POST['body']
		my_image = request.FILES.get('image')
		my_video = request.FILES.get('video')
		post = Post.objects.create(body = body,my_image = my_image,my_video=my_video)
		post.save()
		return redirect('/confession/')
	else:
		return render(request, 'create_post.html')

def post_list(request):
	list = Post.objects.all()
	return render (request,"post_list.html",{"obj_list":list})

def post_detail(request,p_id):
	post = Post.objects.filter(id = p_id).first()
	likes = post.likes.count()
	dislikes = post.dislikes.count()
	comments = post.comments.all()
	if(post.my_image):
		pic = post.my_image.url
		my_url = "/confession"+pic
	else:
		my_url = ""
	if(post.my_video):
		video = post.my_video.url
		my_url1 = "/confession"+video
	else:
		my_url1 = ""
	
	
	
	return render (request,"post_detail.html",{"object":post,"likes":likes,"dislikes":dislikes,"comments":comments,"url":my_url,"url1":my_url1})

def post_like(request,p_id):
	post = Post.objects.filter(id = p_id).first()
	like = Like.objects.create(post = post)
	like.save()
	return HttpResponse('') 

def post_dislike(request,p_id):
	post = Post.objects.filter(id = p_id).first()
	dislike = DisLike.objects.create(post = post)
	dislike.save()
	return HttpResponse('') 
	
def post_comment(request,p_id):
	post = Post.objects.filter(id = p_id).first()	
	response_data = {}
	if request.POST.get('action') == 'post':
		content = request.POST.get('content','nothing to say')
		response_data['content'] = content
		response_data['created_at'] = timezone.localtime(timezone.now()).strftime('%B %d, %Y %I:%M %p')
		print(response_data['content']) 
		print("megha")  
		
		Comment.objects.create(
			post = post,
			content = content
		)    
		return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )                                                                                                                                                                                                                                                    
	return HttpResponse('OK')






