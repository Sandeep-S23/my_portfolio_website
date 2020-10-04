from django.shortcuts import render, get_object_or_404
from . models import Project, Contact
from django.contrib import messages

def index(request):
	return render(request, "portfolio/index.html", {})

def projects(request):
	projects = Project.objects.all()
	context = {
		'projects': projects
	}
	return render(request, "portfolio/projects.html", context)

def viewproject(request, proj_id):
	project = get_object_or_404(Project, pk=proj_id)
	context = {
		'project': project
	}
	return render(request, "portfolio/viewproject.html", context)

def features(request):
	return render(request, "portfolio/features.html", {})

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phno']
		message = request.POST['message']

		contact = Contact(name=name, email=email, phone=phone, message=message)
		contact.save()
		messages.success(request, 'Thanks for showing interest, will get back to you soon.')
	return render(request, "portfolio/contact.html", {})		