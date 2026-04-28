from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Rol de Usuario")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} - {self.role.name if self.role else 'Sin Rol'}"
    
    def save(self, *args, **kwargs):
        # Determine staff status based on role
        if self.role and self.role.name.lower() == 'technical':
            new_staff_status = True
        else:
            new_staff_status = False

        # Only save the User if the status actually changed
        if self.user.is_staff != new_staff_status and not self.user.is_superuser:
            self.user.is_staff = new_staff_status
            # Use update_fields to prevent triggering unrelated signals
            self.user.save(update_fields=['is_staff'])
            
        super().save(*args, **kwargs)

# SIGNALS

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def sync_user_groups(sender, instance, **kwargs):
    if instance.role:
        instance.user.groups.clear()
        instance.user.groups.add(instance.role)

@receiver(m2m_changed, sender=User.groups.through)
def sync_profile_role_from_group(sender, instance, action, pk_set, **kwargs):
    if action == "post_add" or action == "post_remove":
        first_group = instance.groups.first()
        Profile.objects.filter(user=instance).update(role=first_group)