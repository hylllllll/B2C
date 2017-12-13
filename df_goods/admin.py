from django.contrib import admin
from .models import TypeInfo, GoodsInfo


class GoodsInfoInlines(admin.TabularInline):
    """嵌入商品类型管理页面"""

    model = GoodsInfo


@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    """类型Admin"""

    list_display = ['id', 'title', 'is_delete']
    search_fields = ['title']
    list_per_page = 10

    inlines = [GoodsInfoInlines]


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    """商品Admin"""

    list_display = ['id', 'gtitle', 'gprice', 'gabstract', 'gnum', 'gdetail', 'is_delete']
    list_per_page = 20
    search_fields = ['gtitle']


# admin.site.register(TypeInfo, TypeInfoAdmin)
# admin.site.register(GoodsInfo, GoodsInfoAdmin)
