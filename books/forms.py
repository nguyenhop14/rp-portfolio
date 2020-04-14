from .models import Author, Book
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _
class AuthorForm(ModelForm):
  class Meta:
    model = Author
    localized_fields = ('birth_date')
    
    fields = ['name', 'title', 'birth_date']
    labels = {
      'name': _('Writer'),
    }
    help_texts = {
      'name': _('Some useful help text'),
    }
    error_messages = {
      'name': {
        'max_length': _("This writer's name is too long"),
      },
    }
class BookForm(ModelForm):
  class Meta:
    model = Book
    fields = ['name', 'authors']