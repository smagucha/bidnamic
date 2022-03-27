from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.forms import forms

Bidding_Settings_CHOICES = (
    ("HIGH", "HIGH"),
    ("MEDIUM", "MEDIUM"),
    ("LOW", "LOW"),
)


class UserInfo(models.Model):
    title = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    bidding_setting = models.CharField(max_length=6, choices=Bidding_Settings_CHOICES, default='HIGH')
    google_ads_account_id = models.CharField(max_length=50)

    def __str__(self):
        return f"Name: {self.firstname} {self.surname}"

    def clean(self):
        today = date.today()
        age = (today - self.date_of_birth).days // 365
        if age < 18:
            raise forms.ValidationError("you must be eighteen and above")


