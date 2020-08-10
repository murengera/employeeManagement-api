from users.models import User


class Backend(object):

    def authenticate(self, request=None, **kwargs):
        """
        Returns a user with the given credentials
        :param request: Request object passed to the backend
        :param kwargs: Contains credentials to find user
        :return: User if credentials are found
        """
        username = kwargs.get('username')  # Contains national_id or phone_number
        password = kwargs.get('password')

        # Trying national_id
        user = User.objects.filter(national_id=username).first()

        # Trying phone_number
        if not user:
            user = User.objects.filter(phone_number=username).first()

        if user:
            if user.check_password(password):
                return user

        return None

    def get_user(self, user_id):
        """
        Returns instance of the user, when given the user_id
        :param user_id: User id, the current primary key
        :return: User if found and None otherwise
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
