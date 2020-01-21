# Generated by Django 2.2.4 on 2019-12-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino'], ['N', 'Nenhuma das opções']], max_length=1)),
            ],
        ),
    ]
