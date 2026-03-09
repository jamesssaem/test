from django.shortcuts import render
from .models import Kimbab      

def index(request):
    return render(request, "kimbab/index.html")

def kimbab_list(request):
    my_kimbabs = Kimbab.objects.all()
    my_context = {"kimbabs": my_kimbabs}
    return render(request, "kimbab/kimbab_list.html", context=my_context)

def kimbab_search(request):
    search_word = request.POST.get("q", "")   # 검색어 받아오기. POST!   
    print(f"검색어: {search_word}")
    if search_word:
        searched_kimbabs = Kimbab.objects.filter(name__contains=search_word)    # name 필드에 search_word가 포함된 Kimbab 객체들.
    else:
        searched_kimbabs = Kimbab.objects.none()   # 빈 쿼리셋.
    my_context = {"kimbabs": searched_kimbabs}
    return render(request, "kimbab/kimbab_search.html", context=my_context)