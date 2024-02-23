from django.shortcuts import render, redirect
from app_blog import models
from .models import Post, Comentario
from app_blog.forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home (request):
    posts = models.Post.objects.all()
    return render (request, 'home.html', {'posts':posts})


def post_details(request, slug):
    post = models.Post.objects.get(slug=slug)

    if request.method == 'POST':
        nome = request.user.username
        email = request.user.email
        conteudo = request.POST.get('conteudo')

        comentario = Comentario(post=post, nome=nome, email=email, conteudo=conteudo,)
        comentario.save()#salva o comentario no banco
    comentarios = post.comentarios.all()
    return render(request, 'post_details.html', {'post': post, 'comentarios': comentarios})

def index(request):
    return render(request, 'index.html')

#signup page
def user_signup(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})
#login page
def user_login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'login.html',{'form': form})
    #logout page
def user_logout(request):
    logout(request)
    return redirect('home')

def post_admin(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        resumo = request.POST.get('resumo')
        conteudo = request.POST.get('conteudo')
        autor = request.POST.get('autor')
        img = request.POST.get('img')
        slug = request.POST.get('slug')
        
        novo_post = Post(titulo=titulo, resumo=resumo, conteudo=conteudo, autor=autor, img=img, slug=slug)

        novo_post.save()

        return redirect('home')
    return render(request, 'post_admin.html')

def edit_admin(request,slug):
    post = models.Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.resumo = request.POST.get('resumo')
        post.conteudo = request.POST.get('conteudo')
        post.autor = request.POST.get('autor')
        post.img_url = request.POST.get('img_url')
        post.slug = request.POST.get('slug')

        post.save()

        return redirect('home')
    return render(request, 'post_edit.html', {'post': post})

def delete_post(request, slug):
    post = models.Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})
