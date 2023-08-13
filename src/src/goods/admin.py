from django.contrib import admin
from django.contrib.auth.models import Group, User

from src.goods.models import Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    """Админка для модели еды"""

    list_display = (
        "title",
        "price",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "price",
                    "photo",
                )
            },
        ),
    )


admin.site.unregister(Group)
admin.site.unregister(User)

