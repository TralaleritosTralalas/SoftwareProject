# Fresh Watchlist model setup

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_platform_p_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.ManyToManyField(blank=True, related_name='user_lists', to='app.audiovisualcontent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
            options={
                'unique_together': {('user', 'name')},
                'ordering': ['-created_at'],
            },
        ),
    ]