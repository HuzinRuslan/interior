from django.shortcuts import render

menu_list = [
    {'href': 'product_all', 'name': 'ALL'},
    {'href': 'product_home', 'name': 'HOME'},
    {'href': 'product_office', 'name': 'OFFICE'},
    {'href': 'product_furniture', 'name': 'FURNITURE'},
    {'href': 'product_modern', 'name': 'MODERN'},
    {'href': 'product_classic', 'name': 'CLASSIC'},
]


def main(request):
    content = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    content = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contacts.html', content)


def catalog(request):
    content = {
        'title': 'каталог',
        'list_names': menu_list,
    }
    return render(request, 'mainapp/catalog.html', content)


def chair(request):
    content = {
        'title': 'каталог',
        'list_names': menu_list,
    }
    return render(request, 'mainapp/fishnet-chair.html', content)
