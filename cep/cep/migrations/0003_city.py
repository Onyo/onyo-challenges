# Generated by Django 2.1.3 on 2018-11-15 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0002_load_states'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cep.State')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('name', 'state')},
        ),
    ]