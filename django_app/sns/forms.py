from django import forms
from .models import Message,Good, Reply
from django.contrib.auth.models import User

#Messageフォーム
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]
        widgets = {
            "content":forms.TextInput(attrs={"class":"form-control"}),
        }


# プルダウンメニューフォーム
class SortForm(forms.Form):
    data = [
        (1,"新しい順"),
        (2,"人気の投稿"),
        (3,"古い順")
    ]
    choice = forms.ChoiceField(label="並び替え", choices=data, )

#replyフォーム
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["replied"]
        widgets = {
            "replied":forms.TextInput(attrs={"class":"form-control"}),
        }







# #Goodフォーム
# class GoodForm(forms.ModelForm):
#     class Meta:
#         model = Good
#         fields = ["owner","message"]

# #投稿フォーム
# class PostForm(forms.Form):
#     content = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"class":"form-control", "rows":2}))

#     def __init__(self, user, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)