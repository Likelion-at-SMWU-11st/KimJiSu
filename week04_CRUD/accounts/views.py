from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup_view(request):
    # Get 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        # Post 요청 시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)

        if form.is_valid():
            # 회원가입 처리
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')


