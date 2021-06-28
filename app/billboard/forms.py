from django import forms

from .models import Professor

class ProfessorPostForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('professor_in', 'subject_out', 'contact_out', 'contact_out', 'social_out',)
        # professor_in = forms.IntegerField()
