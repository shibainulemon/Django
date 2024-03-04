# class HelloForm(forms.Form):
#     id = forms.IntegerField(label="ID")

from django import forms
from . models import Friend, Message


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["name","mail","gender","age","birthday"]
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "mail":forms.EmailInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "birthday":forms.DateInput(attrs={"class":"form-control"}),
        }



#メッセージフォーム
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["title","content","friend"]
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control form-control-sm"}),
            "content":forms.Textarea(attrs={"class":"form-control form-control-sm"}),
            "friend":forms.Select(attrs={"class":"form-control form-control-sm"}),
        }


class FindForm(forms.Form):
    find = forms.CharField(label = "Find", required=False, \
        widget=forms.TextInput(attrs={"class":"form-control"}))

class CheckForm(forms.Form):
    str = forms.CharField(label = "Name",  \
        widget=forms.TextInput(attrs={"class":"form-control"}))


# from django import forms

# class HelloForm(forms.Form):
#     name = forms.CharField(label = "Name", \
#         widget=forms.TextInput(attrs={"class":"form-control"}))

#     mail = forms.CharField(label = "Eail", \
#         widget=forms.TextInput(attrs={"class":"form-control"}))

#     gender = forms.BooleanField(label = "Gender",required=False, \
#         widget=forms.CheckboxInput(attrs={"class":"form-check"}))

#     age = forms.IntegerField(label = "age", \
#         widget=forms.NumberInput(attrs={"class":"form-control"}))

#     birthday = forms.DateField(label="Birth", \
#         widget=forms.DateInput(attrs={"class":"form-control"}))