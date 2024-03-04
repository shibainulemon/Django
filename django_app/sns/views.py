from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Message,Good
from .forms import MessageForm, SortForm, ReplyForm



# index関数
@login_required(login_url="/admin/login/")
def index(request, page=1):
    max = 10
    form = MessageForm()
    form2 = SortForm()
    form3 = ReplyForm()
    msgs = Message.objects.all()
    # ページネーションで指定ページを取得
    paginate = Paginator(msgs,max)
    page_items = paginate.get_page(page)

    params = {
        "login_user":request.user,
        "form":form,
        "sortform":form2,
        "replyform":form3,
        "contents":page_items,
        "title":"Index",
        "reply_msg":"",
        # "replies":replies,
    }

    if request.method == "POST":
        print("WWWWWWWWWWWWWW",request.POST["reply_id"])
        if "sort_btn" in request.POST:
            ch = request.POST["choice"]
            if ch == "1":
                msgs = Message.objects.all()
            elif ch == "2":
                msgs = Message.objects.all().order_by("-good_count")
            else:
                msgs = Message.objects.all().order_by("pub_date")

            paginate = Paginator(msgs,max)
            page_items = paginate.get_page(page)
            params["contents"] = page_items
            params["sortform"] = SortForm(request.POST)
            # return redirect(to="/sns/")
            return render(request, "sns/index.html", params)

        elif "reply_btn" in request.POST:
            reply_id = request.POST["reply_id"]
            obj = Message.objects.get(id=reply_id)
            reply_content = obj.replies.all()
            # print(obj.replies.replied,"******************")
            form = ReplyForm(request.POST)
            if form.is_valid():
                reply = form.save(commit=False)
                reply.owner = request.user
                reply.message = Message.objects.get(id=reply_id)
                reply.save()
            params["reply_msg"] = reply_content
            return redirect(to="/sns/")
    # return render(request,'sns/index.html',{"reply_msg": reply_content})
    return render(request, "sns/index.html", params)





# goodしたメッセージ一覧を表示する関数
@login_required(login_url="/admin/login/")
def goods(request):
    goods = Good.objects.filter(owner=request.user)

    params = {
        "login_user":request.user,
        "contents":goods,
    }
    return render(request, "sns/good.html", params)



# メッセージ投稿処理の関数
@login_required(login_url="/admin/login/")
def post(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect(to="/sns/")
    else:
        messages = Message.objects.filter(owner=request.user)
        params = {
            "login_user":request.user,
            "contents":messages
        }
    return render(request, "sns/post.html", params)



# good機能処理の関数（Goodテーブルにレコードを追加、Messageテーブルのgood_countに１を加算）
@login_required(login_url="/admin/login/")
def good(request, good_id):
    good_msg = Message.objects.get(id=good_id)
    is_good = Good.objects.filter(owner=request.user) .filter(message=good_msg).count() #goodテーブルのレコードを特定

    if is_good > 0:
        nogood = Good.objects.filter(owner=request.user) .filter(message=good_msg)
        nogood.delete()
        messages.success(request,"goodを解除します。")
        good_msg.good_count -= 1
        good_msg.save()
        # good = Good.objects.get(id=good_id)
        return redirect(to="/sns")
    else:
        good_msg.good_count += 1
        good_msg.save()
        good = Good()
        good.owner = request.user
        good.message = good_msg
        good.save()

    messages.success(request, "このメッセージにgoodしました")
    return redirect(to="/sns")


# 投稿編集の関数
@login_required(login_url="/admin/login/")
def edit(request, num):
    obj = Message.objects.get(id=num)
    if request.method == "POST":
        message = MessageForm(request.POST, instance=obj)
        message.save()
        return redirect(to="/sns/post")
    params = {
        "login_user":request.user,
        "id":num,
        "form":MessageForm(instance=obj),
    }
    return render(request, "sns/edit.html", params)



# 投稿の削除
@login_required(login_url="/admin/login/")
def delete(request, num):
    message = Message.objects.get(id=num)
    if request.method == "POST":
        message.delete()
        return redirect(to="/sns/post")
    params = {
        "title":"Hello,Delete",
        "id":num,
        "obj":message,
    }
    return render(request,"sns/delete.html", params)



# 投稿者を絞り込んでメッセージ表示
@login_required(login_url="/admin/login/")
def find(request,id,page=1):
    # print(id,page)
    max = 3
    form = MessageForm()
    msgs = Message.objects.filter(owner_id=id)
    paginate = Paginator(msgs,max)
    page_items = paginate.get_page(page)

    params = {
        "login_user":request.user,
        "form":form,
        "contents":page_items,
        "title":"Index",
        "id":id,
    }

    return render(request, "sns/find.html", params)