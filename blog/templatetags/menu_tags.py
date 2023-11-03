from django import template
from blog.models import Category


register = template.Library()


# @register.simple_tag()
# def get_categories():
#     return 


@register.inclusion_tag('blog/top_menu.html')
def get_categories():
    category = Category.objects.order_by('name')
    return {"list": category}