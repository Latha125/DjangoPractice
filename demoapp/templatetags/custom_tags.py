from django import template

register=template.Library()

@register.simple_tag
def multiplication(num1,num2):
    return "abcd"