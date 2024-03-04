from django.shortcuts import render
from .forms import HelloForm

def index(request):
  params = {
    'title': 'Hello',
    'message': 'your data:',
    'form': HelloForm(),
    "result": None,
    "goto":'next'
  }
  if (request.method == 'POST'):
    params['message'] = '名前：' + request.POST['name'] + \
      '<br>メール：' + request.POST['mail'] + \
      '<br>年齢：' + request.POST['age'] + \
      '<br>血液型：' + request.POST['choice']
    params['form'] = HelloForm(request.POST)

  return render(request, 'lesson/index.html', params)

def next(request):
  params = {
    'title': '残念！',
    'message':"ここは別のページです。もう一度送信したら元のページに戻るよ",
    'form': HelloForm(request.POST),
    "result": None,
    "goto":'index'
  }
  return render(request, 'lesson/index.html', params)

# from django.shortcuts import render
# from .forms import HelloForm

# def index(request):
#   params = {
#     'title': 'Hello',
#     'message': 'your data:',
#     'form': HelloForm(),
#     "result": None,
#   }
#   if (request.method == 'POST'):
#     params['message'] = '名前：' + request.POST['name'] + \
#       '<br>メール：' + request.POST['mail'] + \
#       '<br>年齢：' + request.POST['age'] + \
#       '<br>血液型：' + request.POST['choice']
#     params['form'] = HelloForm(request.POST)

#   return render(request, 'lesson/index.html', params)

