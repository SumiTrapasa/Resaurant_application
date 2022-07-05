from django.shortcuts import render
from .models import Restuarant, Cuisines, Menu
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
    context = {
        'obj2' : queryset,
        'obj' : queryset2
    }
    return render(request, "restuarant/restuarant_view.html",context)

def items_view(request,id):
    queryset = Cuisines.objects.get(id=id)
    queryset2 =  queryset.cuisine.all()
    context = {
        'title' : queryset,
        'obj' : queryset2
    }
    return render(request, "restuarant/items_view.html",context)
    