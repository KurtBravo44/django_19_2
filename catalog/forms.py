from django import forms
from django.forms import BaseModelFormSet, BaseInlineFormSet

from catalog.models import Product, Version

bad_words=["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name',
                  'description',
                  'image',
                  'category',
                  'price',
                  )

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Нельзя создавать продукт с таким названием: {word}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Нельзя создавать продукт с таким описанием: {word}')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

class VersionFormSet(BaseInlineFormSet):
    def clean(self):

        super().clean()
        cont_cur_version = 0
        for form in self.forms:
            if form['current'].data:
                cont_cur_version += 1
                print('current_version_count', cont_cur_version)
                print('is_current=', form['is_current'])
        if cont_cur_version > 1:
            raise forms.ValidationError('Только одна версия может быть активной')






