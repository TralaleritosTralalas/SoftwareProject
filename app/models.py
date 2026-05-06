from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed

class User(AbstractUser):
    role = models.ForeignKey(
        Group, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Rol de Usuario",
        related_name='user_roles'
    )
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        help_text='The groups this user belongs to.',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return f"{self.username} - {self.role.name if self.role else 'Sin Rol'}"
    
    def save(self, *args, **kwargs):
        if self.role and self.role.name.lower() == 'technical':
            new_staff_status = True
        else:
            new_staff_status = False

        if self.is_staff != new_staff_status and not self.is_superuser:
            self.is_staff = new_staff_status
            self.save(update_fields=['is_staff'])
            
        super().save(*args, **kwargs)

# SIGNALS
@receiver(post_save, sender=User)
def sync_user_groups(sender, instance, **kwargs):
    if instance.role:
        instance.groups.clear()
        instance.groups.add(instance.role)

@receiver(m2m_changed, sender=User.groups.through)
def sync_profile_role_from_group(sender, instance, action, pk_set, **kwargs):
    if action == "post_add" or action == "post_remove":
        first_group = instance.groups.first()
        User.objects.filter(id=instance.id).update(role=first_group)