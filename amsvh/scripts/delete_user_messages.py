from usercomment.models import UserComment


def run():
    user_messages = UserComment.objects.all()
    user_messages.delete()
