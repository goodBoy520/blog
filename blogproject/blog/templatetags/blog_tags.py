from ..models import Post, Category, Tag
from django import template

register = template.Library()

#最新文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]

#归档末班
@register.simple_tag
def get_archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

#分类
@register.simple_tag
def get_categories():
    return Category.objects.all()

#标签
@register.simple_tag
def get_tags():
    return Tag.objects.all()
