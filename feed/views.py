# We use class-based views
from django.views.generic import ListView
from .models import Post  # We import the Post model to use it in the view

# Create your views here.

# This view will render a template with the latest 30 posts
class HomePage(ListView):
    http_method_names = ["get"]  # Only allows GET requests
    template_name = "homepage.html"  # Template to be rendered
    model = Post  # The model this view will use
    context_object_name = "posts"  # The name used to access the posts in the template
    queryset = Post.objects.all().order_by('-id')[:30]  # Return the 30 most recent posts
