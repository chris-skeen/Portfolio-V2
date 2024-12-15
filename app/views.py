from django.shortcuts import render

def main_view(request):
    return render(request, "main.html", {})

def projects_view(request):
    return render(request, "projects.html", {})

def contacts_view(request):
    return render(request, "contacts.html", {})