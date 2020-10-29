# Generated by Django 3.1.1 on 2020-10-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен в обработку'), ('PRD', 'обработан'), ('PD', 'оплачен'), ('RDY', 'готов к выдаче'), ('DN', 'выдан'), ('CNC', 'отменен')], default='FM', max_length=3),
        ),
    ]