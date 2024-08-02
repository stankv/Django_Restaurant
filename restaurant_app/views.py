from django.shortcuts import render

from restaurant_app.models import MenuItem


# Create your views here.
def index(request):
    # считываем блюда из БД, сортируем случайным образом и выводим первые 6
    menu_brk = MenuItem.objects.filter(type__exact='BRK').order_by('?')[:6]
    menu_lun = MenuItem.objects.filter(type__exact='LUN').order_by('?')[:6]
    menu_din = MenuItem.objects.filter(type__exact='DIN').order_by('?')[:6]
    context = {'menu_brk': menu_brk, 'menu_lun': menu_lun, 'menu_din': menu_din}
    return render(
        request,
        'index.html',
        context=context
    )


def about(request):
    return render(
        request,
        'about.html'
    )


def contacts(request):
    return render(
        request,
        'contacts.html'
    )
