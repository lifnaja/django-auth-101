from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'account'

    def ready(self):
        import account.signals # noqa 
