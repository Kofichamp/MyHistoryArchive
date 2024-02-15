from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View
from .forms import UserCreationForm, UserRegisterForm

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        # Optionally, you can add a success message or perform other actions here
        return render(request, 'users/logout.html')

    def post(self, request):
        # Handle POST requests if needed
        pass