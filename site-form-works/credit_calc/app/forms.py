from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.FloatField(label="Стоимость товара", required=True)
    # такой вариант валидации лучше?
    rate = forms.FloatField(label="Процентная ставка",
                            required=True,
                            min_value=0,
                            error_messages={'min_value': 'Процентная ставка не может быть отрицательной'})
    months_count = forms.IntegerField(label="Срок кредита в месяцах",
                                      required=True)

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной либо равной 0")
        return initial_fee

    def clean_months_count(self):
        months_count = self.cleaned_data.get('months_count')
        if not months_count or months_count < 0:
            raise forms.ValidationError("Срок кредита не может быть отрицательным либо равным 0")
        return months_count

    def clean(self):
        # общая функция валидации
        return self.cleaned_data
