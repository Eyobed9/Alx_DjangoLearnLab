from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView  
from .models import User, Post

# Register view
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
# A view for displaying the profile of the user
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'
    
# A view for editing the profile of the user
class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('profile')
    template_name = 'accounts/profile_update.html'
    
    def get_object(self):
        return self.request.user
    
# A view to display all blog posts
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "posts/post_list.html"
    
# A view to show individual blog posts
class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"
    
   # "ListView", "DetailView", "DeleteView"
    