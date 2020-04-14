from django.shortcuts import render
from accounts.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfileInfo
from django.contrib.auth.models import User 
# Create your views here.
def index(request):
  id = 3
  return render(request, 'accounts/index.html')

@login_required
def special(request):
  return HttpResponse("You are logged in")

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('accounts:index'))

def register(request):
  registered = False
  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileInfoForm(data=request.POST)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
      profile = profile_form.save(commit=False)
      profile.user = user 
      if 'profile_pic' in request.FILES:
        print('found it')
        profile.profile_pic = request.FILES['profile_pic']
        profile.save()
        registered = True 
    else:
      print(user_form.errors, profile_form.errors)
  else:
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
  return render(request, 'accounts/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

  
def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
      if user.is_active:
        profile = UserProfileInfo.objects.get(user=user)
        login(request, user)
        return render(request, 'accounts/index.html', {'id': 3})
      else:
        return HttpResponse("Not active")
    else:
      print("Some one tried to login and failed")
      print("They username: {}".format(username))
      return HttpResponse("Invalid")
  else:
    return render(request, 'accounts/login.html',{}) 