from django.shortcuts import render
from django import forms
from ball_calculator import Widths, Lengths

# Create your views here.
class SelectSizeForm(forms.Form):
    lengths = forms.ModelChoiceField(queryset=Ranking.objects.all(), empty_label=None)
    widths = forms.ModelChoiceField(queryset=Ranking.objects.all(), empty_label=None)

def get_template(request):
    form = SelectSizeForm(request.Get)
    volume = None

    if form.is_vald():
        length = form.cleaned_data['length']
        width = form.cleaned.data['width']