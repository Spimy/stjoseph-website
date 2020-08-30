from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        user_model = get_user_model()

        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)

        try:
            user = user_model.objects.get(username__exact=username)
        except user_model.DoesNotExist:
            try:
                user = user_model.objects.get(email__iexact=username)
            except user_model.DoesNotExist:
                return None
            else:
                return user
        else:
            return user
