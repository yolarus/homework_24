from django import template

register = template.Library()


@register.filter()
def media_filter(path: str) -> str:
    if path:
        return f"/media/{path}"
    else:
        return "#"
