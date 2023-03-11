from django.shortcuts import render
from .models import project
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def home(request):
    visits = request.session.get("visits", 0)
    request.session["visits"] = visits + 1
    message = f"Number of visits: {visits + 1}"
    pro = project.objects.all()
    return render(request, "blog/index.html", {"pro": pro, "message": message})


def error_404(request, exception):
    return render(request, "blog/404.html")
