from urllib.parse import quote 
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import View
from .forms import PostForm, UserForm
from .models import Post 



# Create your views here.
# function based views

def post_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	if request.method == 'POST':
		print(request.FILES)
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.success(request,"Successfully created")
			return HttpResponseRedirect(instance.get_absolute_url())

	else:
		context = {
			"form": PostForm(), 
		}
	return render(request, "post_form.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Post,id=id)
	share_string = quote(instance.content)
	context = {
	"title": instance.title,
	"instance": instance,
	"share_string": share_string,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(title__icontains=query)
	page = request.GET.get('page')
	paginator = Paginator(queryset_list, 8)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset,
		"title": "Latest Posts"
	}
	return render(request, "post_list.html", context)


def post_update(request, id=None):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successful Edited")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
	"title": instance.title,
	"instance": instance,
	"form": form,
	}
	return render(request, "post_form.html", context)

def post_delete(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404	
	return HttpResponse("<h1>Delete</h1>")

class UserFormView(View):
	form_class = UserForm
	template_name = 'register_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect("list")

		else:
			print(form.errors)

		return render(request, self.template_name, {'form': form})

def movie(request):
	return render(request, "movies.html", context)
