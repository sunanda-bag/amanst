from captcha.fields import CaptchaField
from django import forms

class YourForm(forms.Form):
    captcha = CaptchaField()

    