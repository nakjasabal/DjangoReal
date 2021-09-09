from django.urls import path
from . import views

# 함수형 뷰 사용
app_name = 'livepolls' 
'''
네임스페이스
<a href="{% url 'polls:detail' question.id %}"> 와 같이 사용한다. 
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),#/livepolls/5/
    path('<int:question_id>/vote/', views.vote, name='vote'),#/livepolls/5/vote/
    path('<int:question_id>/results/', views.results, name='results'),#/livepolls/5/result/    
]