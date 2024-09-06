from django.contrib.admin import ModelAdmin, register
from .models import *


@register(Nobat)
class NobatAdmin(ModelAdmin):
    pass



@register(Khedmat)
class KhedmatAdmin(ModelAdmin):
    pass


@register(Bimar)
class BimarAdmin(ModelAdmin):
    pass