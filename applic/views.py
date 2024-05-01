from django.shortcuts import render, redirect
from .forms import CategoryForm, CommentForm, NewsForm, UserForm
from .models import Comment, News

def detail(request, id):
    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.author = request.user
            com.news = News.objects.get(id=id)
            com.save()
    context = {
        'form': form,
        'Yangilik': News.objects.get(id=id)
    }
    return render(request, 'detail.html', context)

def execise_(request):
    form = UserForm()
    return render(request, 'exercise.html', {'form':form})
def home(request):
    context = {
        'form': News.objects.all()
    }
    return render(request, 'home.html', context)

def create_bolim(request):
    form = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form})

def create_user(request):
    form = UserForm()
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            parol = form.cleaned_data['password']
            user.set_password(parol)
            user.save()
            return redirect('home')
    return render(request , 'create.html', {'form': form})

def create_news(request):
    form = NewsForm()
    if request.POST:
        form = NewsForm(request.POST, files=request.FILES)
        if form.is_valid():
            News.objects.create(
                title = form.cleaned_data['title'],
                matn = form.cleaned_data['matn'],
                bolim = form.cleaned_data['bolim'],
                rasm = form.cleaned_data['rasm'],
                author = request.user
            )
            return redirect('home')
    return render(request , 'create.html', {'form': form})
