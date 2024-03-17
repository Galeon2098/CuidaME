from django.shortcuts import redirect, render
from django.db.models import Q,Count
from main.foro.forms import CommentForm, ThreadForm
from main.foro.models import Comment, Thread

#Crear un nuevo hilo
def new_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            new_thread = form.save(commit=False)
            new_thread.save()
            return redirect('foro:list_threads')
    else:
        form = ThreadForm()
    return render(request, 'new_thread.html', {'form': form})

#Listar hilos
def list_threads(request):
    threads = Thread.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')
    return render(request, 'list_threads.html', {'threads': threads})

#Ver detalles de un hilo
def thread_detail(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)
    comments = Comment.objects.filter(thread_id=thread_id)
    form = CommentForm()
    return render(request, 'thread_detail.html', {'thread': thread, 'comments': comments , 'form': form})

#Comentar en un hilo
def comment(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.thread = thread
            new_comment.save()
            return redirect('foro:thread_detail', thread_id=thread_id)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(thread_id=thread_id)
    return render(request, 'thread_detail.html', {'thread': thread, 'comments': comments, 'form': form})

#Buscar hilos por palabras clave
def search_threads(request):
    search_query = request.POST.get('search_query', '')
    threads = Thread.objects.all()
    if search_query:
        threads = threads.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    return render(request, 'list_threads.html', {'threads': threads, 'search_query': search_query})

#Ordenar hilos por fecha de creación
def order_threads(request):
    threads = Thread.objects.order_by('-date_created')
    return render(request, 'list_threads.html', {'threads': threads})


