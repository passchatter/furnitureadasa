from django.shortcuts import render, redirect
from .models import Produks, Category, Comment
from django.db.models import Q
from .forms import CommentForm


def home(request):
    query = request.GET.get('query', '')
    produks = Produks.objects.all().order_by('-id')[0:10]

    if query:
        produks = produks.filter(Q(title__icontains=query))

    return render(request, 'core/home.html', {
        'produks':produks,
        'query':query
    })



def detail(request, pk):
    produk = Produks.objects.get(pk=pk)
    related = Produks.objects.filter(category = produk.category).exclude(pk=pk)[0:5]
    comments = Comment.objects.filter(produk=pk)
    form = None

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.produk = produk
            comment.user = request.user
            comment.save()

            return redirect('core:detail', pk=produk.id)


    if request.user.is_authenticated:
        form = CommentForm()

    return render(request, 'core/detail.html', {
        'produk':produk,
        'related':related,
        'form':form,
        'comments':comments
    })

def browser(request):
    query = request.GET.get('query', '')
    produks = Produks.objects.all()
    category_id = request.GET.get('category', 0)
    categorys = Category.objects.all()

    if category_id:
        produks = produks.filter(category_id = category_id)

    if query:
        produks = produks.filter(Q(name__icontains=query))

    return render(request, 'core/browser.html', {
        'produks':produks,
        'categorys':categorys,
        'query':query,
        'category_id':int(category_id)
    })


