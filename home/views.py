from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

def custom_404(request, exception):
    """Custom 404 error handler."""
    return render(request, "errors/404.html", status=404)

def custom_500(request):
    """Custom 500 error handler."""
    return render(request, "errors/500.html", status=500)
