from django.forms import ModelForm, TextInput

from .models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
