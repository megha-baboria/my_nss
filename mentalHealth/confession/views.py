# from django.shortcuts import render
# import json
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from friends.models import CustomNotification
# from friends.serializers import NotificationSerializer
# from .forms import PostCreateForm
# from .models import *

# class PostCreateView(CreateView):
#     model = Post
#     http_method_names = ['post']
#     form_class = PostCreateForm
#     template_name = 'home.html'
#     success_url = reverse_lazy('core:home')
#     def form_valid(self, form):
#         if self.request.user.is_authenticated:
#             form.instance.user = self.request.user
#         return super(PostCreateView, self).form_valid(form)
#     def form_invalid(self, form):
#         """If the form is invalid, render the invalid form."""
#         print(form.errors)
#         return redirect(reverse_lazy('core:home'))
#     def post(self, *args, **kwargs):
#         form = self.get_form()
#         self.object = None
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

# def create_comment(request, post_id=None):
#     if request.method == "POST":
#         post = Post.objects.get(id=post_id)
#         comment = post.comments.create(user=request.user, content=request.POST.get('content'))
#         notification = CustomNotification.objects.create(type="comment", recipient=post.user, actor=request.user, verb="commented on your post")
#         channel_layer = get_channel_layer()
#         channel = "comment_like_notifications_{}".format(post.user.username)
#         print(json.dumps(NotificationSerializer(notification).data))
#         async_to_sync(channel_layer.group_send)(
#             channel, {
#                 "type": "notify",
#                 "command": "new_like_comment_notification",
#                 "notification": json.dumps(NotificationSerializer(notification).data)
#             }
#         )
#         return redirect(reverse_lazy('core:home'))
#     else:
#         return redirect(reverse_lazy('core:home'))
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import post_form
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from django.utils import timezone
import json

def post_create(request):
	form = post_form(request.POST or None)	
	if form.is_valid():
		form.save()
		form = post_form()
	context = {"form" : form}
	template_name = 'create_post.html'
	return render (request,template_name,context)

def post_list(request):
	list = Post.objects.all()
	return render (request,"post_list.html",{"obj_list":list})

def post_detail(request,p_id):
	post = Post.objects.filter(id = p_id).first()
	likes = post.likes.count()
	dislikes = post.dislikes.count()
	comments = post.comments.all()
	return render (request,"post_detail.html",{"object":post,"likes":likes,"dislikes":dislikes,"comments":comments})

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






