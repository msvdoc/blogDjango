from django import forms

class MedicineFindForm(forms.Form):
    medicine_name = forms.CharField(label="Название лекарства", help_text="Введи название лекарства", max_length=200)
   
