import re
from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import ValidationError


class DomainRestrictedAdapter(DefaultAccountAdapter):
    """
    An adapter class that restricts email registration to a specific domain.

    This adapter extends DefaultAccountAdapter to enforce domain-based email
    validation, ensuring users can only register with an email from Merley
    Hillstone College.

    Attributes:
        allowed_domains (list): List of permitted domain names

    Methods:
        __init__(*args, **kwargs): Initializes the adapter with specified
        allowed domain.
        clean_email(email): Validates email addresses against allowed domains

    Raises:
        ValidationError: When attempting to register with an unauthorized
        domain
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = ["merleyhillstone.net"]

    def clean_email(self, email):
        domain = email.split("@")[-1].lower()
        if domain not in self.allowed_domains:
            raise ValidationError(
                f"Please use your school email address"
                f"(i.e. JohnDoe123@{', '.join(self.allowed_domains)})"
            )
        return email
