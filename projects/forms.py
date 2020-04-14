from django.forms import ModelForm, inlineformset_factory
from .models import Project, Dev 

DevFormset = inlinefromset_factory(Project, Dev, fields=('name', 'age'))