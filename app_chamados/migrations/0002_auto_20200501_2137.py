# Generated by Django 3.0.3 on 2020-05-02 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_chamados', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='status',
        ),
        migrations.AddField(
            model_name='chamado',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_chamados.Pendencia'),
        ),
    ]