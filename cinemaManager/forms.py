from django import forms
from cinemaManager.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("title","age_rating","duration","description",)  
        