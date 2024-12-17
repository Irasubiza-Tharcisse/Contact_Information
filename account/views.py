from django.shortcuts import render
from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def login_F(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_active = authenticate(username=username, password=password)
    if user_active is not None and user_active.is_staff:
      login(request,user_active)
      return redirect('profile')
    elif user_active is not None and not user_active.is_staff:
      login(request,user_active)
      return redirect('user_profile')
      
    messages.error(request, f'hello {username}, check your username and password')
    return render(request, 'account/login.html')
  else:
    messages.error(request, 'invalid username or password')
    return render(request, 'account/login.html')


def login_view(request):
    return render(request, 'account/login.html')


#logout
def logout_view(request):
  logout(request)
  return redirect('login_page')


#Admin dashboard 
@login_required
def admin_profile_view(request):
  user_active = request.user
  context={
    'username': user_active.username,
  }
  return render(request, 'account/admin_profile.html',context)


# user profile
def user_profile_view(request):
  user_active = request.user
  context={
    'username': user_active.username,
    'email': user_active.email,
    'first_name': user_active.first_name,
    'last_name': user_active.last_name,
  }
  return render(request, 'account/user_profile.html',context)



#create account
def signup_view(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirmpassword = request.POST.get('confirmpassword')

    if User.objects.filter(username=username).exists():
      messages.error(request, f'username {username} already exists, try again')
      return render(request, 'account/signup.html')
    else:
      if password == confirmpassword:
        user = User.objects.create_user(username=username,email=email,password=password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        login(request,user)
        return render(request,'account/login.html')
      else:
        messages.error(request, 'passwords do not match')
        return render(request, 'account/signup.html')
    
  return render(request, 'account/signup.html')
      
    
# view all users
@login_required
def all_users_view(request):
  users = User.objects.all()
  user_active = request.user
  context={
    'username': user_active.username,
    'users': users,
  }
  return render(request, 'account/all_users.html',context)


#edit user
@login_required
def edit_user_view(request, user_id):
  user = get_object_or_404(User, id=user_id)
  user_active = request.user
  context={
    'username': user_active.username,
    'user': user,
  }
  if request.method == 'POST':
    user.username = request.POST.get('username')
    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.email = request.POST.get('email')
    user.password = request.POST.get('password')
    user.save()
    messages.success(request, f'Account for {user.username} was updated successfully')
    if hasattr(user_active, 'is_staff') and user_active.is_staff:
       return redirect('all_users')
    else:
      return redirect('user_profile')
  elif hasattr(user_active, 'is_staff') and user_active.is_staff:
     return render(request,'account/confirm_edit.html',context)
  else:
    return render(request,'account/confirm_edit_user.html',context)

#delete account
def delete_user(request, user_id):
  user = get_object_or_404(User, id=user_id)
  user_active = request.user
  context ={
    'username': user_active.username,
  }
  if request.method == 'POST':
      user.delete()
      messages.success(request, 'User deleted successfully!')
      if hasattr(user_active, 'is_staff') and user_active.is_staff:
        return redirect('all_users')  # Redirect to the user management page
      else:
        return redirect('login') 

  elif hasattr(user_active, 'is_staff') and user_active.is_staff:
     return render(request,'account/confirm_delete.html',context)
  else:
    return render(request,'account/confirm_delete_user.html',context)
  


#settings
def settings_view(request):
  user_active = request.user
  context={
    'username': user_active.username,
    'email': user_active.email,
    'first_name': user_active.first_name,
    'last_name': user_active.last_name,
  }
  if hasattr(user_active, 'is_staff') and user_active.is_staff:
    return render(request, 'account/settings.html', context)
  else:
      return render(request, 'account/settings.html', context)

  
