from django.shortcuts import render

def home_view(request):
    template_view = "index.html"
    
    return render(request, template_name=template_view)

