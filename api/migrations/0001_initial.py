# Generated by Django 4.1.7 on 2023-04-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('thumbnail_url', models.TextField(blank=True, null=True)),
                ('descripton', models.TextField(blank=True, null=True)),
                ('date_create', models.TextField(blank=True, null=True)),
                ('like', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Album',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('follow', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True, null=True)),
                ('alias', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Artist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artistsong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'ArtistSong',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Playlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlistbyuser',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True, null=True)),
                ('creator', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PlaylistByUser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlistbyusersong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PlaylistByUserSong',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlistsong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'PlaylistSong',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlistuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_id', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PlaylistUser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('audio', models.TextField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True, null=True)),
                ('like', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Song',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Topic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.TextField(primary_key=True, serialize=False)),
                ('passwd', models.TextField()),
                ('name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usersongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('islike', models.BooleanField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('recenly_listen_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'UserSongs',
                'managed': False,
            },
        ),
    ]