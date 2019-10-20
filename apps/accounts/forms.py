from django import forms

from .models import User

class LoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        # grab form data
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        # checking authentification
        if email and password:
            try:
                user=User.objects.get(email=email)
            except:
                user=None

            """
            The following bunch of if, else if statements will return errors if the following
            cases are met
            -- Login is not valid
            -- Login is currently not active
            """
            if ((not user) or (not user.check_password(password))):
                raise forms.ValidationError("L'email ou le mot de passe est incorrect")
            elif (not user.is_active):
                raise forms.ValidationError("Vérifier votre email ou contacter le service technique. Votre compte est désactivé")

        return super(LoginForm, self).clean()
