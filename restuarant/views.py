from django.shortcuts import render, get_object_or_404
from .models import Restuarant, Cuisines, Menu
from .forms import ResForm, CuisForm, MenuForm
# Create your views here.

def restuarant_details_view(request):
    queryset = Restuarant.objects.all()

    context = {
        'obj' : queryset
    }
    return render(request, "restuarant/restuarant_list.html", context)

def restuarant_view(request,id):
    queryset= Restuarant.objects.get(id=id)
    queryset2= queryset.cuisines.all()
    queryset3 = queryset.rname.all()
    context = {
        'obj2' : queryset,
        'obj' : queryset2,
        'obj3': queryset3
    }
    return render(request, "restuarant/restuarant_view.html",context)

def items_view(request,id):
    queryset = Menu.objects.get(id=id)
    # queryset2 =  queryset.cuisine.all()
    context = {
        'obj1' : queryset
        # 'obj' : queryset2
    }
    return render(request, "restuarant/items_view.html",context)
    
def res_create(request):
    form =  ResForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ResForm()
    context = {
        'form' : form
    }
    return render(request, "restuarant/res_create.html", context)

def res_update(request, id=id):
    obj = get_object_or_404(Restuarant, id=id)
    form =  ResForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ResForm()
    context = {
        'form' : form
    }
    return render(request, "restuarant/res_create.html", context)

def res_delete(request, id):
    obj = get_object_or_404(Restuarant, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object" : obj
    }
    return render(request, "restuarant/res_delete.html", context)
