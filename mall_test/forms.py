from django import forms
from mall_test.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["name", "amount"]
