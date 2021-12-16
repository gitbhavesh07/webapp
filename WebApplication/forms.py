from django import forms

from .models import uploadfile


class UploadForm(forms.ModelForm):
    class Meta:
        model = uploadfile
        fields = ('Name', 'Pdf')

from .models import graphinput

class EditForms(forms.ModelForm):
     class Meta:
           model=graphinput
           fields= "__all__"