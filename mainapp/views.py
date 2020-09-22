from django.shortcuts import render


def main(request):
    text = 'da'
    content = {
        'title': 'главная',
        "test": text,
        'items_list': [1, 2, 3, 4, 5],
        'user': {
            'first_name': 'max',
            'date_birth': '12/04/2000',
        }
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    return render(request, 'mainapp/contacts.html')


def catalog(request):
    return render(request, 'mainapp/catalog.html')


def chair(request):
    return render(request, 'mainapp/fishnet-chair.html')
