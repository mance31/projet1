from django.forms.models import ModelForm
from .models import Student,Presence
#from django.contrib.auth.forms import UserChangeForm

class StudentForm(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Student

    # liste des champs A Editer
  
    fields  = (
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    )

class callform(ModelForm):
  class Meta:
    # la ref du ModEle
    model = Presence

    # liste des champs A Editer
    fields =(
      "date_call",
      "ismissing",
      "Reasson",
      "student", 
    )

class cursuscallform(ModelForm):
  class Meta:
    model = Presence
    fields=(
      "date_call",
      "ismissing"
    )

