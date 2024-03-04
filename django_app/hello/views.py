from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend, Message
from .forms import FriendForm,FindForm,CheckForm, MessageForm
from django.db.models import Count,Sum,Avg,Min,Max
from django.core.paginator import Paginator


def index(request, num=1):
    data = Friend.objects.all().order_by("-age")
    re1 = Friend.objects.aggregate(Count("age"))
    re2 = Friend.objects.aggregate(Sum("age"))
    re3 = Friend.objects.aggregate(Avg("age"))
    re4 = Friend.objects.aggregate(Min("age"))
    re5 = Friend.objects.aggregate(Max("age"))
    msg = f"count{re1["age__count"]}<br>\
            sum:{re2["age__sum"]}<br>\
            avg:{re3["age__avg"]}<br>\
            min:{re4["age__min"]}<br>\
            max:{re5["age__max"]}"

    #ページネーターのview設定
    data = Friend.objects.all()
    page = Paginator(data,3)
    params ={
        "title":"Hello,Paginator",
        "message":"5件ごとに表示中",
        "data":page.get_page(num),
    }
    return render(request, "hello/index.html", params)






#新規レコード作成
def create(request):
    params = {
        "title":"Hello,create",
        "form": FriendForm(),
    }
    if (request.method == "POST"):
        friend = FriendForm(request.POST) #ディクショナリが引数
        friend.save()
        return redirect(to="/hello")  #htmlを開くための関数 renderはparamsを使わないと動的なデータを渡せない。to引数にurlを渡す
    return render(request,"hello/create.html", params)






#更新
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == "POST"):
        friend = FriendForm(request.POST, instance=obj) 
        friend.save()
        return redirect(to="/hello")
    params = {
        "title":"Hello,Edit",
        "id":num,
        "form": FriendForm(instance=obj),
    }
    return render(request,"hello/edit.html", params)






#削除
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == "POST"):
        # friend = FriendForm(request.POST, instance=obj) 
        friend.delete()
        return redirect(to="/hello")
    params = {
        "title":"Hello,Delete",
        "id":num,
        "obj":friend,
    }
    return render(request,"hello/delete.html", params)





#検索
def find(request):
    if (request.method == "POST"):
        form = FindForm(request.POST)
        find = request.POST["find"]
        list = find.split()
        data = Friend.objects.all()[int(list[0]):int(list[1])]
        msg = f"Result:{str(data.count())}"
    else:
        msg = "検索中・・・"
        form = FindForm()
        data = Friend.objects.all()
    params = {
        "title":"Hello,Search",
        "message":msg,
        "form":form,
        "data":data,
    }
    return render(request,"hello/find.html", params)




#バリデーションチェック
def check(request):
    params = {
        "title":"Hello,Check!",
        "message":"check validation",
        "form": FriendForm(),
    }
    if (request.method == "POST"):
        form = FriendForm(request.POST)
        params["form"] = form
        if (form.is_valid()):
            params["message"] = "OK!"
        else:
            params["message"] = "no good・・・"
    return render(request,"hello/check.html", params)



#ページネーション
def message(request, page=1):
    if (request.method == "POST"):
        form = MessageForm(request.POST)
        form.save()
    data = Message.objects.all()
    paginator = Paginator(data,5)
    params = {
        "title":"Message",
        "form": MessageForm(),
        "data":paginator.get_page(page),
    }
    return render(request,"hello/message.html", params)





    # if (request.method == "POST"):
    #     name = request.POST["name"]
    #     mail = request.POST["mail"]
    #     gender = "gender" in request.POST
    #     age = request.POST["age"]
    #     birth = request.POST["birthday"]

    #     friend = Friend(name=name,mail=mail,gender=gender,age=age,birthday=birth)
    #     friend.save()
    #     return redirect(to="/hello")
    # return render(request,"hello/create.html", params)




# def index(request):
#     data = Friend.objects.all()
#     params = {
#         "title":"Hello",
#         "message":"all friends",
#         "data":[],
#         "form":HelloForm(),
#     }

#     if (request.method == "POST"):
#         num = request.POST["id"]
#         item = Friend.objects.get(id=num)
#         params["data"]=[item]
#         params["form"]=HelloForm(request.POST)
#     else:
#         params["data"]= Friend.objects.all()

#     return render(request, "hello/index.html", params)











# from django.shortcuts import render
# # from django.http import HttpResponse
# from django.views.generic import FormView
# from .forms import HelloForm

# class IndexView(FormView):
#     template_name = 'hello/index.html'
#     form_class = HelloForm
#     #success_url = '/'
#     def __init__(self):
#         self.params={
#             'title': 'Hello',
#             'message': 'your data:',
#             'form': self.form_class(),
#         }
#     def get(self,request):
#         return render(self.request, self.template_name, self.params)


#     def form_valid(self, form):
#         self.params["message"] = '名前：{}<br>メール：{}<br>年齢：{}'.format(
#             form.cleaned_data['name'],
#             form.cleaned_data['mail'],
#             form.cleaned_data['age']
#         )
#         print(self.request.POST)
#         self.params['form'] = self.form_class(self.request.POST)
#         return render(self.request, self.template_name, self.params)




# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import HelloForm

# def index(request):
#     params = {
#         "title":"Hello/Index",
#         "msg":"お名前は？",
#     }
#     return render(request,"hello/index.html",params)

# def form(request):
#     msg = request.POST["msg"]
#     params = {
#         "title":"Hello/Form",
#         "msg":"こんにちは"+ msg + "さん。",
#         }
#     return render(request, "hello/index.html", params)

# def index(request):
#     params = {
#         "title":"Hello",
#         "message":"データを入力してください。:",
#         "form":HelloForm()
#     }

#     if (request.method == "POST"):
#         params["message"] = "名前" + request.POST["name"] + \
#             "<br>メール：" + request.POST["mail"] + \
#             "<br>年齢：" + request.POST["age"]

#         params["form"] = HelloForm(request.POST)

#     return render(request, "hello/index.html", params)
