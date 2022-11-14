# Generated by Django 4.0.5 on 2022-08-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEmailaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254, unique=True)),
                ('verified', models.IntegerField()),
                ('primary', models.IntegerField()),
            ],
            options={
                'db_table': 'account_emailaddress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountEmailconfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('key', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'account_emailconfirmation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdjuntarArchivos',
            fields=[
                ('iddocumento', models.AutoField(primary_key=True, serialize=False)),
                ('registro_fotografico', models.CharField(max_length=45)),
                ('soat', models.CharField(max_length=45)),
                ('tecnomecanico', models.CharField(max_length=45)),
                ('identificacion_propietario', models.CharField(max_length=45)),
                ('tarjeta_propiedad', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'adjuntar_archivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CargarDocumento',
            fields=[
                ('iddocumento', models.AutoField(primary_key=True, serialize=False)),
                ('certificado_alcoholemia', models.CharField(max_length=45)),
                ('certificado_sustancias_psicoactivas', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'cargar_documento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('idconductor', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('correo_electronico', models.CharField(max_length=30, unique=True)),
                ('numero_identificacion', models.CharField(max_length=15, unique=True)),
                ('fecha_expedicion_documento', models.DateField()),
                ('lugar_expedicion_documento', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=10, unique=True)),
                ('telefono_alterno', models.CharField(max_length=10, unique=True)),
                ('tipo_identificacion_idtipo_identificacion', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'conductor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('iddepartamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=90)),
                ('codigo', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'django_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('idmunicipio', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paradero',
            fields=[
                ('idparadero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'paradero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlanRodamiento',
            fields=[
                ('idplan_rodamiento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('inicio_ruta', models.CharField(max_length=30)),
                ('numero_vehiculo', models.PositiveIntegerField(blank=True, null=True)),
                ('numero_ruta', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'plan_rodamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('idruta', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_ruta', models.CharField(max_length=30)),
                ('retorno_ruta', models.CharField(max_length=30)),
                ('fin_ruta', models.CharField(max_length=30)),
                ('numero_ruta', models.PositiveIntegerField()),
                ('distancia_kilometros', models.PositiveIntegerField()),
                ('tiempo_estimado', models.CharField(blank=True, max_length=15, null=True)),
                ('numero_vueltas', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ruta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=30)),
                ('uid', models.CharField(max_length=191)),
                ('last_login', models.DateTimeField()),
                ('date_joined', models.DateTimeField()),
                ('extra_data', models.TextField()),
            ],
            options={
                'db_table': 'socialaccount_socialaccount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=40)),
                ('client_id', models.CharField(max_length=191)),
                ('secret', models.CharField(max_length=191)),
                ('key', models.CharField(max_length=191)),
            ],
            options={
                'db_table': 'socialaccount_socialapp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialappSites',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'socialaccount_socialapp_sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialtoken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('token_secret', models.TextField()),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'socialaccount_socialtoken',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubirArchivos',
            fields=[
                ('iddocumento', models.AutoField(primary_key=True, serialize=False)),
                ('documento_identidad', models.CharField(max_length=45)),
                ('experiencia_laboral', models.CharField(max_length=45)),
                ('licencia_conduccion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'subir_archivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('idturno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'db_table': 'turno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('idubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('longitud', models.FloatField()),
                ('latitud', models.FloatField()),
            ],
            options={
                'db_table': 'ubicacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idvehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('numero_orden', models.PositiveIntegerField(unique=True)),
                ('numero_licencia_transito', models.CharField(max_length=30, unique=True)),
                ('nombre_propietario', models.CharField(max_length=45)),
                ('identificacion_propietario', models.CharField(max_length=15, unique=True)),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('marca', models.CharField(max_length=20)),
                ('linea', models.CharField(max_length=20)),
                ('modelo', models.PositiveIntegerField()),
                ('capacidad_personas', models.PositiveIntegerField()),
                ('clase_vehiculo', models.CharField(max_length=20)),
                ('cilindraje', models.FloatField()),
                ('numero_chasis', models.CharField(max_length=20, unique=True)),
                ('tipo_combustible', models.CharField(max_length=10)),
                ('numero_motor', models.CharField(max_length=20, unique=True)),
                ('tipo_carroceria', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('vin', models.CharField(max_length=20, unique=True)),
                ('numero_ejes', models.IntegerField()),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
    ]