from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(attrs={"accept": "image/*"}),
        required=False,
    )

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
            "picture",
        )

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name and len(first_name) < 3:
            raise forms.ValidationError(
                "First name must be at least 3 characters long.",
                code="invalid",
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if last_name and len(last_name) < 3:
            raise forms.ValidationError(
                "Last name must be at least 3 characters long.",
                code="invalid",
            )
        return last_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label=_("first name"),
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        label=_("last name"),
        required=True,
        min_length=3,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Já existe este email", code="invalid")

        return email


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Required.",
        error_messages={
            "min_length": "Please, add more than to letters.",
        },
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Required.",
        error_messages={
            "min_length": "Please, add more than to letters.",
        },
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=True,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=_("Use the same password as before."),
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "Já existe este email", code="invalid"
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if password1:
            password_validation.validate_password(password1)

        return password1

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    "password2",
                    forms.ValidationError("Passwords are different!"),
                )

        return super().clean()

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get("password1")

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user
