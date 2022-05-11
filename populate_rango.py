import os
from unicodedata import category
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title':'official python tutorial',
        'url': 'http://docs.python.org/3/tutorial/'},
        {'title':'how to think like a computer scientit',    
        'url': 'http://www.greenteapress.com/thinkpython/' },
        {'title':'Google',
        'url': 'http://google.com.pa/'},
         {'title':'youtube',
        'url': 'http://youtube.com/'},
         {'title':'github',
        'url': 'http://github.com/'},
        {'title':'gitkrkaken',
        'url': 'http://gitkraken.com/'}
    ]
    django_pages = [
        {'title':'oficial django tutorial',
        'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial101/'},
        {'title':'django wikipedia',
        'url': 'https://es.wikipedia.org/wiki/Django_(framework)/'}
    ]
    other_pages = [
        {'title':'flask',
        'url': 'https://flask.pocoo.org'}
    ]

    cats = {'Python':{'pages': python_pages},
    'Django': {'pages': django_pages},
    'Other Frameworks': {'pages': other_pages}}





    for cat, cat_data in cats.items():
        c=add_cat(cat)
        for p in cat_data['pages']:
            add_page(c,p['title'], p['url'])


    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}' )

def add_page(cat, title, url, views=0):
    p= Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__=='__main__':
    print('starting population script...')
    populate()