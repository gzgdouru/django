from .models import User

class EmailBackend(object):
    def authenticate(self, request, **kwargs):
        email = kwargs.get("email", kwargs.get("username"))
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(kwargs["password"]):
                return user

    #这个方法必须实现
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
