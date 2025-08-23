from .forms import ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.views.generic.edit import UpdateView  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

# Register view
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_201_CREATED)


# Login view
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

    
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
