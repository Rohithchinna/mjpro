# Generated by Django 5.1.3 on 2025-01-09 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_networks_alter_users_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_seen', models.BooleanField(default=False)),
                ('notif_content', models.TextField()),
                ('notif_send_time', models.DateTimeField(auto_now_add=True)),
                ('notif_received_time', models.DateTimeField()),
                ('notif_from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notif_from_user', to='main.users')),
                ('notif_to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notif_to_user', to='main.users')),
            ],
        ),
    ]
