# signals.py

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Post
from .utils import detect_and_replace_offensive

@receiver(pre_save, sender=Post)
def preprocess_post_content(sender, instance, **kwargs):
    # Replace offensive words in the content field
    instance.content = detect_and_replace_offensive(instance.content)
