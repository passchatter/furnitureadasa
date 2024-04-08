from django.shortcuts import render, redirect, get_object_or_404
from core.models import Produks, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import NewProdukForm

@login_required
def dashboard(request):
    produks = Produks.objects.filter(create_by = request.user)
    categorys = Category.objects.all()
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)

    if category_id:
        produks = produks.filter(category_id = category_id)
        
    if query:
        produks = produks.filter(Q(name__icontains=query))

    return render(request, 'dashboard/index.html', {
        'produks':produks,
        'categorys':categorys,
        'query':query,
        'category_id':int(category_id)
    })

@login_required
def addproduk(request):

    if request.method == 'POST':
        form = NewProdukForm(request.POST, request.FILES)
        if form.is_valid():
            produk = form.save(commit=False)
            produk.create_by = request.user
            produk.save()
            return redirect('/dashboard')
    else:
        form = NewProdukForm()

    return render(request, 'dashboard/newproduk.html', {
        'form':form,
        'title':'add produk'
    })


@login_required
def updateproduk(request, pk):
    produk = get_object_or_404(Produks, pk=pk, create_by=request.user)

    if request.method == 'POST':
        form = NewProdukForm(request.POST, request.FILES, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = NewProdukForm(instance=produk)

    return render(request, 'dashboard/newproduk.html', {
        'form':form,
        'title':'update produk'
    })


def deleteproduk(request, pk):
    produk = get_object_or_404(Produks, pk=pk)
    produk.delete()

    return redirect('/dashboard')