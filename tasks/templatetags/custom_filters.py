from django import template

register = template.Library()

@register.filter
def next_order_dir(value, current_order_by):
    if value == current_order_by:
        return 'asc' if current_order_by.startswith('-') else 'desc'
    return 'asc'
