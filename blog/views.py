
from django.shortcuts import render
from .models import project
# Create your views here.
def home(request):
    pro=project.objects.all()
    return render(request, 'blog/index.html',{'pro':pro})

def error_404(request,exception):
    return render(request, 'blog/404.html')