from django import forms

from apps.ff_core.models import FFLPlayer

class FFLPlayerForm(forms.ModelForm):
    class Meta:
        model = FFLPlayer
        exclude = ('league', 'user')
#class ItemForm(forms.Form):
#    listing = forms.ChoiceField(choices=LISTING_TYPES, initial='T')
#    name = forms.CharField(max_length=255)
#    category = forms.ModelChoiceField(Category.objects.all())
#    department = forms.CharField(max_length=255)
#    description = forms.CharField(widget=forms.Textarea)
