from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """Завершение сеанса с пользователем"""
    logout(request)
    return HttpResponseRedirect(reverse('leaning_logs:index'))

def register(request):
    """Регистрация нового пользователя"""
    if request.method != 'POST':
        #Display blank registration form.
        form = UserCreationForm()
    else:
        #Обработка заполненой формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Выполнение входа пользователя
            auth_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, auth_user)
            return HttpResponseRedirect(reverse('leaning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)