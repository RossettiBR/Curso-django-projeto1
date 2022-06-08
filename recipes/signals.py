from django.db.models.signals import post_save
from django.dispatch import receiver
from recipes.models import Recipe


@receiver(post_save, sender=Recipe)
def recipe_post_signal(sender, instance, created, *args, **kwargs):
    ....