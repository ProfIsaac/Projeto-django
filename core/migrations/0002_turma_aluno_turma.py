# Generated by Django 4.0.4 on 2022-06-03 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.turma'),
            preserve_default=False,
        ),
    ]