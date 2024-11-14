from django import forms
from .models import CompFirstYear, BeedFirstYear

class CompFirstYearForm(forms.ModelForm):
    class Meta:
        model = CompFirstYear
        fields = [
            'instructor_id',
            'program_id',
            'course_code',
            'course_name',
            'department',
            'credit_hours',
            'prerequisites',
            'school_year',
            'semester',
        ]  # You can adjust this list based on your needs



class BeedFirstYearForm(forms.ModelForm):
    class Meta:
        model = BeedFirstYear
        fields = [
            'instructor_id',
            'program_id',
            'course_code',
            'course_name',
            'department',
            'credit_hours',
            'prerequisites',
            'school_year',
            'semester',
        ]  # You can adjust this list based on your needs


