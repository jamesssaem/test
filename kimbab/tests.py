#
# 테스트.
# 주의: 별도의 테스트 데이터베이스가 생성되어 실제 데이터베이스에는 영향이 없다.
#       python manage.py test kimbab
#

from django.test import TestCase
from django.urls import reverse
from .models import Kimbab

class KimbabModelTest(TestCase):
    """김밥 모델 테스트"""
    
    def test_kimbab_creation(self):
        """김밥 객체 생성 및 문자열 표현 테스트"""
        kimbab = Kimbab.objects.create(
            name="돈카츠김밥",
            price=5500,
            calories=470
        )
        self.assertEqual(str(kimbab), "돈카츠김밥")
        self.assertEqual(kimbab.price, 5500)
        self.assertEqual(kimbab.calories, 470)


class KimbabListViewTest(TestCase):
    """김밥 목록 뷰 테스트"""
    
    def setUp(self):
        """테스트 데이터 준비"""
        Kimbab.objects.create(name="참치김밥", price=3000, calories=350)
        Kimbab.objects.create(name="치즈김밥", price=3500, calories=400)
    
    def test_kimbab_list_view(self):
        """김밥 목록 페이지 정상 작동 테스트"""
        response = self.client.get(reverse('kimbab:kimbab_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "참치김밥")
        self.assertContains(response, "치즈김밥")
        self.assertEqual(len(response.context['kimbabs']), 2)


class KimbabSearchViewTest(TestCase):
    """김밥 검색 뷰 테스트"""
    
    def setUp(self):
        """테스트 데이터 준비"""
        Kimbab.objects.create(name="참치김밥", price=3000, calories=350)
        Kimbab.objects.create(name="치즈김밥", price=3500, calories=400)
        Kimbab.objects.create(name="야채김밥", price=2500, calories=280)
    
    def test_kimbab_search_with_query(self):
        """검색어로 김밥 검색 테스트"""
        response = self.client.post(reverse('kimbab:kimbab_search'), {'q': '치'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "참치김밥")
        self.assertContains(response, "치즈김밥")
        self.assertNotContains(response, "야채김밥")
        self.assertEqual(len(response.context['kimbabs']), 2)
