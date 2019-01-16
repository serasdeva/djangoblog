from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Имя Пользователя")
    password = forms.CharField(label = "пароль",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Имя Пользователя")
    password = forms.CharField(max_length=20,label = "пароль",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Проверка Пароля",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Пароли Не Совпадают")

        values = {
            "username" : username,
            "password" : password
        }
        return values


