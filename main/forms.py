from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        return f' {name.upper()}'

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'count', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name',
                                           'data-rule': 'minlen:4'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email',
                                             'data-rule': 'minlen:4'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Your Phone',
                                            'data-rule': 'minlen:4'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Date',
                                           'data-rule': 'minlen:4'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'id': 'time', 'placeholder': 'Time',
                                           'data-rule': 'minlen:4'}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'id': 'people', 'placeholder': '# of people',
                                              'data-rule': 'minlen:4'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Message'})

        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'date': 'Date',
            'time': 'Time',
            'count': '# of people',
            'comment': 'Message'
             }
        help_texts = {
            'name': 'Please enter at least 4 chars',
            'email': 'Please enter a valid email',
            'phone': 'Please enter at least 4 chars',
            'date': 'Please enter at least 4 chars',
            'time': 'Please enter at least 4 chars',
            'count': 'Please enter at least 1 chars',
        }
        error_messages = {
            'name': {
                'required': 'Це поле е ',
            }
        }
