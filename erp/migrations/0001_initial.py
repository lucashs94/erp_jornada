# Generated by Django 4.1.3 on 2022-12-03 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=50)),
                ('remuneracao', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'tb_funcionario',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'tb_produto',
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.funcionario')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.produto')),
            ],
            options={
                'db_table': 'tb_venda',
            },
        ),
    ]
