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

class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmation du mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_password2(self):
        # check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passes ne correspondent pas")
        return password2

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True # send confirmation email
        if commit:
            user.save()
        return user
