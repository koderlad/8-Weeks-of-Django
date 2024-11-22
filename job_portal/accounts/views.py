from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationFrom
from .models import UserProfile
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            #Create a User Profile Instance
            user_type = form.cleaned_data['user_type']
            UserProfile.objects.create(user=user, user_type=user_type)
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationFrom()
    return render(request, 'accounts/register.html', {'form': form})

def profile(response):
    return render(response, 'accounts/profile.html', {'data': response})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'