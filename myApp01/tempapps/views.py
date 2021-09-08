from django.shortcuts import render
from django.http import HttpResponseRedirect
from tempapps.forms import QuestionForm



def index(request): 
    return render(request, 'index.html')



 
def templateFilter(request):
    num1 = 100
    num2 = 200
    engStr = "nakja's MustHave\r\njava <b>web</b>programming"
    hanStr = "낙자쌤의 자바 웹 프로그래밍"
   
    context = {'num1': num1, 'num2': num2, 
                'engStr': engStr, 'hanStr': hanStr}
    return render(request, 'template_filter.html', context)




def templateTag(request):
    # 리스트(List) 내에 딕셔너리(Dictionary) 인자 반복
    books = [
        {"name":"자바", "price":1000},
        {"name":"HTML", "price":2000},
        {"name":"JSP", "price":3000}
    ]
    hobbys = []
    favorites = ['운동','공부','여행','경제']
    iVar = range(1,11) 

    context = {'books':books, 'hobbys':hobbys, 'favorites':favorites, 'iVar':iVar}
    return render(request, 'template_tag.html', context)




 
#question_create 함수는 forms.py 에서 작성한 QuestionForm 클래스를 사용한다. 
#render 함수에 전달한 {'form': form}은 템플릿에서 질문 등록시 사용할 
# 폼 엘리먼트를 생성할 때 쓰인다.
 
def formCreate(request): # 클래스명이나 URL패턴에 대한 이름을 차후 변경하자.

    # POST 방식이면 데이터가 담긴 제출된 폼으로 간주한다. 
    if request.method == 'POST':
        # request 에 담긴 데이터로 클래스 폼을 생성한다. 
        form = QuestionForm(request.POST)

        # 폼에 담긴 데이터가 유효한지 체크
        if form.is_valid():
            # 폼 데이터가 유효하면, 데이터는 cleaned_data로 복사됨
            new_name = form.cleaned_data['user_id']
            # 리다이렉트
            return HttpResponseRedirect('/thanks/')
    # POST방식이 아닐때 이므로 GET방식. 최초 페이지 요청시            
    else:
        form = QuestionForm()

    return render(request, 'form_create.html', {'form':form})



def thanks(request): 
    return render(request, 'thanks.html')

 