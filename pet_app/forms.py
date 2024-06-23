from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=15, label='Name your pet', widget=forms.TextInput(attrs={'placeholder': 'Enter pet name'}))

class InteractionForm(forms.Form):
    ACTIONS = [
        ('feed', 'Кормить'),
        ('play', 'Играть'),
        ('rest', 'Спать'),
    ]
    action = forms.ChoiceField(choices=ACTIONS, widget=forms.RadioSelect)
