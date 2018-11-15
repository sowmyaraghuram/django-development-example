from django import template

register = template.Library()

@register.filter(name='stripe')
def stripe(value,args):
    return value.replace(args,'')
