from django.db import models
from . import messages
# Create your models here.


class SiteUserPreferences():
    def validation(self, username, email, password1, password2):
        if len(username) < 4:
            return messages.usernameError
        if email.find("@") == -1:
            return  messages.emailError
        if len(password1) < 6:
            return messages.passwordError
        if password1 and password2 and password1 != password2:
                return messages.diffrentPasswordsError
        return None  # Все хорошо!
