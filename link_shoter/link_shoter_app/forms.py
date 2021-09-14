
from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['input_link'].widget.attrs.update(size='40', placeholder="Вставьте вашу ссылку сюда")
        self.fields['input_link'].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Link
        fields = ['input_link', ]


