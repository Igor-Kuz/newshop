from collections import defaultdict

from django import template
from django.utils.safestring import mark_safe

from specs.models import ProductFeatures

register = template.Library()

# @register.filter
