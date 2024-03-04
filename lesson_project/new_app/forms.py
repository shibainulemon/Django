from django import forms
from . models import Members, Post, Category


class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ["username","phone","age","mail"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","category","content","members"]
        widgets = {
            "title": forms.TextInput(attrs={"classs":"form-control form-control-sm"}),
            "category": forms.Select(attrs={"classs":"form-control form-control-sm"}),
            "content": forms.Textarea(attrs={"classs":"form-control form-control-sm"}),
            "member": forms.Select(attrs={"classs":"form-control form-control-sm"}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category"]
        widgets = {
            "title": forms.TextInput(attrs={"classs":"form-control form-control-sm"}),}

# class FindForm(forms.Form):
#     find = forms.CharField(label="Find",required=False,\
#             widget=forms.TextInput(attrs={'class':'form-control'}))

class SortForm(forms.Form):
    data = [
        ("趣味","趣味"),
        (2,"ペット"),
        (3,"ファッション"),
        (4,"音楽"),
        (5,"IT"),
    ]
    choice = forms.ChoiceField(label="カテゴリー選択",choices=data)