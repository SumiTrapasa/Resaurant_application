from django.shortcuts import render, get_object_or_404, redirect
from .models import Restuarant, Cuisines, Menu
from .forms import ResForm, CuisForm, MenuForm
from django.http import HttpResponseRedirect
# Create your views here.

def restuarant_details_view(request):
    restuarant = Restuarant.objects.all()
    cuisines= Cuisines.objects.all()
    context = {
        'restuarant' : restuarant,
        'cuisines' : cuisines
    }
    return render(request, "restuarant/restuarant_list.html", context)

def restuarant_view(request,id):
    restuarant= Restuarant.objects.get(id=id)
    cuisines= restuarant.cuisines.all()
    menu = restuarant.menu_items.all()
    context = {
        'restuarant' : restuarant,
        'cuisines' :cuisines,
        'menu': menu
    }
    return render(request, "restuarant/restuarant_view.html",context)

def items_view(request,id):
    menu = Menu.objects.get(id=id)
    # queryset2 =  queryset.cuisine.all()
    context = {
        'menu' : menu
        # 'obj' : queryset2
    }
    return render(request, "restuarant/items_view.html",context)
    
def res_create(request):
    form =  ResForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = ResForm()
        return redirect('../')
    context = {
        'form' : form
    }
    return render(request, "restuarant/res_create.html", context)

def res_update(request, id=id):
    obj = get_object_or_404(Restuarant, id=id)
    form =  ResForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # form = ResForm()
        return redirect('../')
    context = {
        'form' : form
    }
    return render(request, "restuarant/res_create.html", context)

def res_delete(request, id):
    restuarant = get_object_or_404(Restuarant, id=id)
    if request.method == "POST":
        restuarant.delete()
        return redirect('../../')
    context = {
        "restuarant" : restuarant
    }
    return render(request, "restuarant/res_delete.html", context)

def item_update(request, res_id, menu_id):
    restuarant = Restuarant.objects.get(id=res_id)
    obj = get_object_or_404(Menu, id=menu_id)
    form =  MenuForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # form = MenuForm()
        return redirect('../../')
        # return HttpResponseRedirect('../items/')
    context = {
        'form' : form,
        "restuarant":restuarant
    }
    return render(request, "menu/menu_create.html", context)

def item_delete(request, res_id, menu_id):
    restuarant = Restuarant.objects.get(id=res_id)
    menu = get_object_or_404(Menu, id=menu_id)
    if request.method == "POST":
        menu.delete()
        return redirect('../../')
        # return HttpResponseRedirect('')
    context = {
        "menu" : menu,
        "restuarant":restuarant
    }
    return render(request, "menu/menu_delete.html", context)

def item_create(request,res_id):
    restuarant = Restuarant.objects.get(id=res_id)
    form =  MenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = MenuForm()
        return redirect('../')
    context = {
        'form' : form
    }
    return render(request, "menu/menu_create.html", context)

def cuis_view(request, res_id, cuis_id):
    restuarant = Restuarant.objects.get(id=res_id)
    menu_items= restuarant.menu_items.all()
    cuisine = Cuisines.objects.get(id=cuis_id)
    items = menu_items.filter(cuisines_type=cuisine)
    context = {
        'cuisine' : cuisine, 
        'items' : items,
        'restuarant':restuarant
    }
    return render(request, "cuisines/cuis_item.html", context)

def cuis_delete(request, res_id, cuis_id):
    restuarant = Restuarant.objects.get(id=res_id)
    cuisine = get_object_or_404(Cuisines, id=cuis_id)
    if request.method == "POST":
        cuisine.delete()
        return redirect('../../../')
        # return HttpResponseRedirect('')
    context = {
        "cuisine" : cuisine,
        "restuarant" : restuarant
    }
    return render(request, "cuisines/cuis_delete.html", context)

def cuis_create(request):
    form =  CuisForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = CuisForm()
        return redirect('../../')
    context = {
        'form' : form
    }
    return render(request, "cuisines/cuis_create.html", context)
    
