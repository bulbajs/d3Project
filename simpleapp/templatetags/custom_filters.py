from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'rub': '₽',
   'usd': '$',
}


@register.filter()
def currency(value, key='rub'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CURRENCIES_SYMBOLS[key]

   return f'{value} {postfix}'


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()
