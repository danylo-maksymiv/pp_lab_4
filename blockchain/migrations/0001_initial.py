# Generated by Django 4.2.16 on 2024-12-13 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('block_hash', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('finalized', 'Finalized'), ('attested', 'Attested'), ('proposed', 'Proposed'), ('pending', 'Pending'), ('uncle', 'Uncle'), ('orphaned', 'Orphaned'), ('invalid', 'Invalid')], db_column='status', max_length=10)),
                ('timestamp', models.DateTimeField()),
                ('epoch', models.PositiveIntegerField()),
                ('slot', models.PositiveIntegerField()),
                ('reward', models.DecimalField(decimal_places=0, max_digits=28)),
                ('difficulty', models.DecimalField(decimal_places=0, max_digits=28)),
                ('state_root', models.CharField(max_length=64, unique=True)),
                ('withdrawal_root', models.CharField(max_length=64)),
                ('height', models.BigIntegerField()),
                ('nonce', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'block',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_address', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'contract',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_hash', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'transaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Validator',
            fields=[
                ('validator_id', models.AutoField(primary_key=True, serialize=False)),
                ('eth_staked', models.DecimalField(decimal_places=0, max_digits=28)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], db_column='status', max_length=8)),
                ('slashed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'validator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('eth_balance', models.DecimalField(decimal_places=0, default=0, max_digits=28)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='ContractData',
            fields=[
                ('contract', models.OneToOneField(db_column='contract_address', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blockchain.contract')),
                ('source_code', models.TextField()),
                ('bytecode', models.TextField()),
                ('name', models.CharField(max_length=255, null=True)),
                ('version', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contract_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mempool',
            fields=[
                ('transaction', models.OneToOneField(db_column='transaction_hash', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blockchain.transaction')),
            ],
            options={
                'db_table': 'mempool',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('contract', models.OneToOneField(db_column='contract_address', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blockchain.contract')),
                ('symbol', models.CharField(max_length=255)),
                ('supply', models.DecimalField(decimal_places=0, max_digits=65)),
                ('decimals', models.PositiveSmallIntegerField()),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionData',
            fields=[
                ('transaction', models.OneToOneField(db_column='transaction_hash', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blockchain.transaction')),
                ('status', models.CharField(choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('failed', 'Failed'), ('canceled', 'Canceled'), ('dropped', 'Dropped'), ('replaced', 'Replaced')], max_length=10)),
                ('value', models.DecimalField(decimal_places=0, max_digits=28)),
                ('eth_price', models.FloatField()),
                ('gas_limit', models.BigIntegerField()),
                ('base_fee', models.DecimalField(decimal_places=0, max_digits=28)),
                ('max_fee', models.DecimalField(decimal_places=0, max_digits=28)),
                ('priority_fee', models.DecimalField(decimal_places=0, max_digits=28)),
                ('input_data', models.TextField(null=True)),
                ('timestamp', models.DateTimeField()),
                ('gas_used', models.BigIntegerField()),
            ],
            options={
                'db_table': 'transaction_data',
                'managed': False,
            },
        ),
    ]
