from django.shortcuts import render

def login_view(request):
    template_view = "login.html"
    
    return render(request, template_name=template_view)

