from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import CustomUser, Transaction, Goal
from datetime import date

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}))
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'class': 'form-input', 'rows': 3}))
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'bio', 'password1', 'password2')
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'transaction_type', 'date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'amount': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'transaction_type': forms.Select(attrs={'class': 'form-input'}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'category': forms.TextInput(attrs={'class': 'form-input'}),
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'target_amount': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'deadline': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }

    def clean_deadline(self):
        from datetime import date
        deadline_value = self.cleaned_data.get('deadline')
        if deadline_value and deadline_value < date.today():
            raise forms.ValidationError('Deadline must be today or a future date.')
        return deadline_value
        
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'phone_number', 'date_of_birth', 'bio'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})
