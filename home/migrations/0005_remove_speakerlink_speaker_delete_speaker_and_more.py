# Generated by Django 4.1.5 on 2023-01-06 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_speaker_speakerlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speakerlink',
            name='speaker',
        ),
        migrations.DeleteModel(
            name='Speaker',
        ),
        migrations.DeleteModel(
            name='SpeakerLink',
        ),
    ]