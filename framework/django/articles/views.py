from django.shortcuts import render

# Create your views here.
# 특정 경로에 대한 처리를 해줄 함수
# 매개변수 이름은 내 마음대로 지어도 됨
# framework 쓸떄는 되도록 convention 지키자
# request : 사용자의 요청에 대한 모든 정보
def index(request):
    # articles 앱의 메인 페이지를 사용자에게 전달
    # render 함수의 두번째 인자 template_name은 정확히는 tmplate이 위치한 경로
    return render(request, 'index.html')