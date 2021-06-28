from django import forms

from .models import Professor

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('professor_data', 'subject_data', 'contact_data', 'email_data', 'social_data',)
        widgets = {'professor_data': forms.TextInput(attrs={'size': 50}),
                   'subject_data': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
                   'contact_data': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
                   'email_data': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
                   'social_data': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
                 }