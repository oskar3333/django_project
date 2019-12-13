from django.shortcuts import render
from django.views.generic import FormView

from .models import Post, Tag
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login

def Main(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'mainPage/main.html', context={'posts': posts, 'tags': tags})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    tags = Tag.objects.all()
    return render(request, 'mainPage/post_detail.html', context={'post': post, 'tags': tags})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'mainPage/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    tags = Tag.objects.all()
    return render(request, 'mainPage/tag_detail.html', context={'tag': tag, 'tags': tags})

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/accounts/login"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)