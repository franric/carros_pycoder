from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
  if request.method == "POST":
    user_form = UserCreationForm(request.POST)
    if user_form.is_valid():
      user_form.save()
      return redirect('login')
  else:
    user_form = UserCreationForm()
  return render(request, 'register.html', {"user_form": user_form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()         # o form já autentica internamente
            login(request, user)
            return redirect('cars_list')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'login_form': form})


def logout_view(request):
    logout(request)
    return redirect('cars_list')

# def login_view(request):
#   if request.method == "POST":
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login(request, user)
#       return redirect('cars_list')
#     else:
#       login_form = AuthenticationForm()
#   else:
#     login_form = AuthenticationForm()
#   return render(request, 'login.html', {'login_form': login_form})
