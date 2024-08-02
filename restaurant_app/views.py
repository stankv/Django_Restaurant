from django.shortcuts import render

from restaurant_app.models import MenuItem
from restaurant_app.forms import ContactForm


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
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'contacts.html',
        context=context
    )
