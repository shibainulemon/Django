from django.shortcuts import render,redirect
from .models import Members,Post,Category
from .forms import MembersForm,PostForm,CategoryForm,SortForm
from django.core.paginator import Paginator



#トップページIndex関数
def index(request):
    data = Post.objects.all()
    params = {
    'title': 'Hello,NewAPP',
    'message': '投稿一覧',
    'data': data,
    "form": SortForm(),
    }
    if (request.method == "POST"):
        # params["data"] = Post.objects.all().order_by("pub_date")
        ch = request.POST["choice"]
        ct=Category.objects.get(category=ch)
        item = Post.objects.filter(category_id=ct.id)
        params["data"]=item
        print(ch)
        if ch == "1":
            print(item)
            params["data"] = [item]
        # elif ch == "2":
        #     params["data"] = Post.objects.all().order_by("-category")
        # else:
        #     params["data"] = Post.objects.all().order_by("members.username")
        params["form"]=SortForm(request.POST)
    return render(request, 'new_app/index.html', params)


#投稿ビュー（PostView）関数
def post(request):
    if (request.method == "POST"):
        post = PostForm(request.POST)
        post.save()
        return redirect(to="/newapp")
    params = {
        "title":"新規投稿",
        "form": PostForm(),
        "categoryform": CategoryForm(),
    }
    return render(request, "new_app/post.html", params)

def category_add(request):
    if request.method == "POST":
        catadd = CategoryForm(request.POST)
        catadd.save()
        return redirect(to="/post")


#投稿ビュー（PostView）関数
# def post(request):
#     if (request.method == "POST"):
#         member = MembersForm(request.POST)
#         member.save()
#         return redirect(to="/")
#     params = {
#         "title":"新規投稿",
#         "form": MembersForm(),
#     }
#     return render(request, "new_app/post.html", params)


# #検索ビュー（search)関数
# def find(request):
#     if (request.method == "POST"):
#         form = FindForm(request.POST)
#         find = request.POST["find"]
#         data = Members.objects.filter(username__contains=find)
#         msg = f"{data.count()}件ヒット"
#     else:
#         msg = "検索中・・・"
#         form = FindForm()
#         data = Members.objects.all()
#     params = {
#         "title":"検索フォーム",
#         "message":msg,
#         "form":form,
#         "data":data,
#     }
#     return render(request, "new_app/search.html", params)