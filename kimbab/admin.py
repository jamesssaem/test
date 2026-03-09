from django.contrib import admin
from .models import Kimbab

# 커스텀 admin 옵션.
class MyKimbabAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')    # 리스트 화면에 name, price 컬럼 출력.
    search_fields = ('name',)           # name 검색창 제공.

# 등록.
admin.site.register(Kimbab, MyKimbabAdmin)