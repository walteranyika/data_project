from django import forms

from main_app.models import Employee

GENDERS = [
    ("Male", "Male"),
    ("Female", "Female"),
]

TEAMS = [
    ("manu", "Manchester United"),
    ("arsenal", "Arsenal"),
    ("chelsea", "Chelsea"),
    ("newcastle", "Newcastle"),
]


class EmployeeForm(forms.ModelForm):
#     gender = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.RadioSelect,
#         choices=GENDERS,
#     )
#
#     teams = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=TEAMS
#     )

    class Meta:
        model = Employee
        fields = "__all__"
