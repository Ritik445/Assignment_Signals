import time
import threading  
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    # Question 1 Synchronously Executed Signals
    print("Signal received. Starting heavy processing...")
    time.sleep(5)  
    print("Signal processing complete.")

    # Question 2 Same Thread Execution
    print(f"Signal running in thread: {threading.current_thread().name}")

    # Question 3 Same Database Transaction
    print(f"Signal received, user: {instance.username}")
    instance.username = 'newusername'
    instance.save(update_fields=['username'])  # This prevents the recursion issue
