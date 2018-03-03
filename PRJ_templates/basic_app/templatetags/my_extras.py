from django import template

register = template.Library()

@register.filter(name='cutString')
def filterCutString(value,args):
    return value.replace(args,' ')
