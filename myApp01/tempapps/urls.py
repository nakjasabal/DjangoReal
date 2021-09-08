from django.urls import path
from . import views

# 함수형 뷰 사용
app_name = 'tempapps'
urlpatterns = [
    path('', views.index, name='index'),
    path('template.filter/', views.templateFilter), #템플릿 필터
    path('template.tag/', views.templateTag), #템플릿 태그
    path('form.create/', views.formCreate, name='formCreate'), # 폼 사용하기
    path('thanks/', views.thanks),  
]