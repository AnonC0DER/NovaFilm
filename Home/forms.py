from django.db import models
from .models import comments, comments_serial
from django.forms import ModelForm, widgets

# comments class
class CommentsForm(ModelForm):
    class Meta:
        model = comments
        fields = ['name', 'body']

        label = {
            'name' : 'Your Name',
            'body' : 'Add a comment'
        }
    
    # set the class (css/style) for fields
    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'form_title'})


# comments class for serial page
class CommentsFormSerial(ModelForm):
    class Meta:
        model = comments_serial
        fields = ['name', 'body']

        label = {
            'name' : 'Your Name',
            'body' : 'Add a comment'
        }
    
    # set the class (css/style) for fields
    def __init__(self, *args, **kwargs):
        super(CommentsFormSerial, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'form_title'})