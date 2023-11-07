from django import forms

from main_app.models import Employee

GENDERS = [
    ("Male", "Male"),
    ("Female", "Female"),
]

TEAMS = [
    ("Manchester United", "Manchester United"),
    ("Arsenal", "Arsenal"),
    ("Chelsea", "Chelsea"),
    ("Newcastle", "Newcastle"),
]


class EmployeeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDERS, widget=forms.RadioSelect())
    team = forms.ChoiceField(choices=TEAMS, widget=forms.CheckboxSelectMultiple())
    teams = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TEAMS,
    )

    class Meta:
        model = Employee
        fields = ["name", "email", "dob", "gender", "salary", "disabled", "profile", "teams"]
        widgets = {
            "dob": forms.DateInput(attrs={"min": "1990-01-01", "type": "date", "max": "2005-12-31"}),
            "salary": forms.NumberInput(attrs={"min": 10000, "max": 60000})
        }
        labels = {
            "name": "Full Names",
        }
        help_texts = {
            "name": "Your Full Name.",
        }
        error_messages = {
            "name": {
                "max_length": "This user's name is too long.",
            },
        }
