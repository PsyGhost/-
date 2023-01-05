from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDERS)
    # 5 <= fullname's length <= 60
    if forms.CharField(min_length=5, max_length=60).istitle():
        full_name = forms.CharField(min_length=5, max_length=60)
    height = forms.IntegerField(
        min_value=70, max_value=250)     # 70 <= height <= 250
    age = forms.IntegerField(
        min_value=14, max_value=99)        # 14 <= age <= 99

    # implement full_name validation function here
    # full_name should be a title
