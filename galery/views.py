from django.contrib.auth.views import password_change, password_reset, password_reset_confirm, password_reset_complete
from django.http import Http404
from django.template import RequestContext
from django.views.generic import DetailView, TemplateView, UpdateView
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from .forms import MyUserCreationForm, ImageForm
from .models import *
from django.core.urlresolvers import reverse_lazy


# ------------------------------------------------------------------------------------------
# авторизация
def login_view(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "* Your username and password combination do not match any of our accounts."
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


# ------------------------------------------------------------------------------------------
def logout_view(request):
    logout(request)
    return redirect('/')


# ------------------------------------------------------------------------------------------
# регистрация нового пользователя
def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = MyUserCreationForm()
    if request.POST:
        new_user_form = MyUserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = authenticate(username=new_user_form.cleaned_data['username'],
                                    password=new_user_form.cleaned_data['password2'],)
            login(request, new_user)
            return redirect('/')
        else:
            print(new_user_form.errors)
            args['form'] = new_user_form
    return render_to_response('register.html', args)


# ------------------------------------------------------------------------------------------
# смена пароля
def change_password(request):
    template_response = password_change(request, template_name='registration/password_change_form.html',
                                        post_change_redirect='profile')
    return template_response


# ------------------------------------------------------------------------------------------
# восстановление пароля
def reset_password(request):
    template_response = password_reset(request, template_name='registration/password_reset_form.html',
                                       post_reset_redirect='password_reset_done')
    return template_response


class PasswordResetDone(TemplateView):
    template_name = 'registration/password_reset_done.html'


def reset_password_confirm(request):
    template_response = password_reset_confirm(request, template_name='registration/password_reset_confirm.html',
                                               post_reset_redirect='password_reset_complete')
    return template_response


def reset_password_complete(request):
    template_response = password_reset_complete(request, template_name='registration/password_reset_complete.html')
    return template_response


# ------------------------------------------------------------------------------------------
# личный кабинет
class Profile(DetailView):
    model = Users
    template_name = 'account/account.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    def get_object(self, queryset=None):
        return self.request.user


# ------------------------------------------------------------------------------------------
# загрузка изображений
def upload_files(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Images(imagefile=request.FILES['imagefile'], uploaded_by=request.user)
            new_image.save()

            return redirect('/galery/')
    else:
        form = ImageForm()

    all_images = Images.objects.all()
    user_images = Images.objects.filter(uploaded_by=request.user.id)
    other_user_images = Images.objects.filter(uploaded_by=request.user)
    users = Users.objects.all()

    return render(request, 'upload.html', {'all_images': all_images, 'user_images': user_images, 'other_user_images': other_user_images,
                                           'form': form, 'users': users}, RequestContext(request))


# ------------------------------------------------------------------------------------------
# изменение данных пользователя
class UsersUpdate(UpdateView):
    model = Users
    fields = ['last_name', 'first_name', 'email', 'phone_number', 'country',
              'index', 'city', 'street', 'house', 'apartment']
    template_name = 'account/users_update_form.html'

    def get_success_url(self):
        return reverse_lazy('profile')


# ------------------------------------------------------------------------------------------
# домашняя страница
class HomeView(TemplateView):
    template_name = 'home.html'


# ------------------------------------------------------------------------------------------
# страница с картинками другого пользователя
def other_user_profile(request, username=""):
    if username:
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise Http404
        photos = Images.objects.filter(uploaded_by=user.id)
        return render(request, 'other_user.html', {'user': user, 'photos': photos})
