from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Register model form
class Register(UserCreationForm):
    # if the username is already registered doesn't go on next step
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError('The given email is already registered !')
    
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name' : 'Full Name'
        }

    # set the class (css/style) for fields
    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'sign__input'})



# Profile Model form
class ProfileUser(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username']

    # set the class (css/style) for fields
    def __init__(self, *args, **kwargs):
        super(ProfileUser, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'sign__input'})