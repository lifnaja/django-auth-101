
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import Profile
from .tokens import account_activation_token


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        if not instance.is_superuser or not instance.is_staff:
            instance.is_active = False
            send_comfirmations_signup(instance, )

        instance.save()
        instance.profile.save()


def send_comfirmations_signup(user):
    current_site = Site.objects.get_current()
    subject = 'Activate Your MySite Account'
    message = render_to_string('emails/activete_account.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    user.email_user(subject, message)
