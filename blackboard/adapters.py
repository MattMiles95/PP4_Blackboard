import re
from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import ValidationError

class DomainRestrictedAdapter(DefaultAccountAdapter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = ['merleyhillstone.net'] 

    def clean_email(self, email):
        domain = email.split('@')[-1].lower()
        if domain not in self.allowed_domains:
            raise ValidationError(f"Please use your school email address (i.e. JohnDoe123@{', '.join(self.allowed_domains)})")
        return email