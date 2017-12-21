Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\dylan.barker> cd .\Dev\ecommerce\
PS C:\Users\dylan.barker\Dev\ecommerce> .\Scripts\activate
(ecommerce) PS C:\Users\dylan.barker\Dev\ecommerce> python manage.py shell
C:\Users\dylan.barker\Dev\ecommerce/Scripts\python.exe: can't open file 'manage.py': [Errno 2] No such file or directory
(ecommerce) PS C:\Users\dylan.barker\Dev\ecommerce> cd .\src\
(ecommerce) PS C:\Users\dylan.barker\Dev\ecommerce\src> python manage.py shell
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from tags.models import Tag
>>> Tag.objects.all()
<QuerySet [<Tag: Make up>, <Tag: add ons>, <Tag: hair>]>
>>> Tag.objects.last()
<Tag: hair>
>>> hair = Tag.objects.last()
>>> hair.title
'hair'
>>> hair.slug
'hair'
>>> hair.active
True
>>> hair.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x0000011A29363128>
>>> hair.products.all()
<ProductQuerySet [<Product: Hair Styling>]>
>>> hair.products.all().first()
<Product: Hair Styling>
>>> exit()
(ecommerce) PS C:\Users\dylan.barker\Dev\ecommerce\src> python manage.py shell
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> qs = Product.objects.all()
>>> qs
<ProductQuerySet [<Product: Add-Ons>, <Product: Makeup Artistry>, <Product: Hair Styling>, <Product: Products>]>
>>> Add-Ons = qs.first()
  File "<console>", line 1
SyntaxError: can't assign to operator
>>> addons = qs.first()
>>> addons
<Product: Add-Ons>
>>> addons.title
'Add-Ons'
>>> addons.description
'Specialty bridal party packages, full day hair and makeup touch-ups, clip-in extension implementation, false lashes, etc. Contact for specific details and complete price list.'
>>> addons.tag
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tag'
>>> addons.tags
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tags'
>>> addons.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x00000285C1B4F940>
>>> addons.tag_set.all()
<QuerySet [<Tag: add ons>]>
>>> addons.tag_set.filter(title__iexact='addons')
<QuerySet []>
>>>