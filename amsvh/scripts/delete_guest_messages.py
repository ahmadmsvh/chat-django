from guestcomment.models import Guest


def run():
    guest_messages = Guest.objects.all()
    guest_messages.delete()
