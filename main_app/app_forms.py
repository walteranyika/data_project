from django import forms

from main_app.models import Employee

GENDERS = [
    ("Male", "Male"),
    ("Female", "Female"),
]

TEAMS = [
    (1, "Manchester United"),
    (2, "Arsenal"),
    (3, "Chelsea"),
    (4, "Newcastle"),
]


class EmployeeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDERS, widget=forms.RadioSelect())
    # team = forms.ChoiceField(choices=TEAMS, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Employee
        fields = ["name", "email", "dob", "gender", "salary", "disabled", "profile"]
        widgets = {
            "dob": forms.DateInput(attrs={"min": "1990-01-01", "type": "date", "max": "2005-12-31"}),
            "salary": forms.NumberInput(attrs={"min": 10000, "max": 60000})
        }
        labels = {
            "name": "Full Names",
        }
        # help_texts = {
        #     "name": "Your Full Name.",
        # }
        error_messages = {
            "name": {
                "max_length": "This user's name is too long.",
            },
        }
