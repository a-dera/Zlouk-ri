# Generated by Django 3.1.2 on 2020-10-23 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zlou', '0002_auto_20201019_1609'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Key',
            new_name='Keys',
        ),
        migrations.RenameField(
            model_name='keys',
            old_name='key',
            new_name='keys',
        ),
        migrations.RenameField(
            model_name='keys',
            old_name='key_date',
            new_name='keys_date',
        ),
        migrations.AlterModelTable(
            name='Words',
            table=None,
        ),
    ]
