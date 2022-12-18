from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, RegisterForm



# страница пользователя
def me(request):
     # если не авторизован, то редирект на страницу входа
    if not request.user.is_authenticated:
        return redirect('login')
    # рендерим шаблон и передаем туда объект пользователя

    return render(request, 'authentication/me.html', {'user': request.user})

# выход
def doLogout(request):
    print('logouttt22')
    # вызываем функцию django.contrib.auth.logout и делаем редирект на страницу входа
    logout(request)
    
    print(request.user.is_authenticated, 'logout')
    return redirect('main:login')


# страница входа
def loginPage(request):

    # инициализируем объект класса формы
    form = LoginForm()

    # обрабатываем случай отправки формы на этот адрес
    if request.method == 'POST':
        
        # заполянем объект данными, полученными из запроса
        form = LoginForm(request.POST)
        # проверяем валидность формы
        if form.is_valid():
            # пытаемся авторизовать пользователя
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # если существует пользователь с таким именем и паролем,
                # то сохраняем авторизацию и делаем редирект
                login(request, user)
                return render(request, 'authentication/me.html', {'user': request.user})
            else:
                # иначе возвращаем ошибку
                form.add_error(None, 'Неверные данные!')

    # рендерим шаблон и передаем туда объект формы
    if (request.user.is_authenticated):
        return render(request, 'authentication/me.html', {'user': request.user})
    return render(request, 'authentication/login.html', {'form': form})


# регистрация
def registerPage(request):

    # инициализируем объект формы
    form = RegisterForm()

    if request.method == 'POST':
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)

        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
           
            user.save()
            
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('main:login')
    # ренедерим шаблон и передаем объект формы
   
    # ренедерим шаблон и передаем объект формы
    return render(request, 'authentication/register.html', {'form': form})



