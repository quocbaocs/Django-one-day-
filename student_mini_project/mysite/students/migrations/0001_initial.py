# Generated by Django 3.0.4 on 2020-03-18 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentNo', models.CharField(db_column='student_no', max_length=20, unique=True)),
                ('studentName', models.CharField(db_column='student_name', max_length=50)),
                ('address', models.CharField(db_column='address', max_length=100)),
            ],
        ),
    ]
