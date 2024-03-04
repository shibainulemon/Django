from django import forms

class HelloForm(forms.Form):
  name = forms.CharField(label='name', \
    widget=forms.TextInput(attrs={'class':'form-control'}))
  mail = forms.CharField(label='mail', \
    widget=forms.TextInput(attrs={'class':'form-control'}))
  age = forms.IntegerField(label='age', \
    widget=forms.NumberInput(attrs={'class':'form-control'}))

  data=[
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ("O","O"),
  ]
  choice = forms.ChoiceField(label='Blood type', \
    choices=data, widget=forms.RadioSelect())
  
  
# from django import forms

# class HelloForm(forms.Form):
#   name = forms.CharField(label='name', \
#     widget=forms.TextInput(attrs={'class':'form-control'}))
#   mail = forms.CharField(label='mail', \
#     widget=forms.TextInput(attrs={'class':'form-control'}))
#   age = forms.IntegerField(label='age', \
#     widget=forms.NumberInput(attrs={'class':'form-control'}))

#   data=[
#     ('A', 'A'),
#     ('B', 'B'),
#     ('AB', 'AB'),
#     ("O","O"),
#   ]
#   choice = forms.ChoiceField(label='Blood type', \
#     choices=data, widget=forms.RadioSelect())
