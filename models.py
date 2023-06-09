# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)
    date_create = models.TextField(blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    cate = models.ForeignKey('Category', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Album'


class Artist(models.Model):
    id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    follow = models.IntegerField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    alias = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Artist'


class Artistalbum(models.Model):
    artist = models.ForeignKey(Artist, models.DO_NOTHING)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ArtistAlbum'


class Artistsong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING, blank=True, null=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ArtistSong'


class Category(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'


class Categorysong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING)
    cate = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CategorySong'


class Playlist(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    topic = models.ForeignKey('Topic', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Playlist'


class Playlistbyuser(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistByUser'


class Playlistbyusersong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING)
    playlist = models.ForeignKey(Playlistbyuser, models.DO_NOTHING)
    date_add = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistByUserSong'


class Playlistsong(models.Model):
    song = models.ForeignKey('Song', models.DO_NOTHING, blank=True, null=True)
    playlist = models.ForeignKey(Playlist, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistSong'


class Playlistuser(models.Model):
    user = models.ForeignKey(Playlistbyuser, models.DO_NOTHING, blank=True, null=True)
    playlist_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaylistUser'


class Song(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    audio = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    listen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Song'


class Songlistenweek(models.Model):
    id = models.AutoField()
    lastlisten = models.DateField(db_column='lastListen', blank=True, null=True)  # Field name made lowercase.
    totallisten = models.IntegerField(db_column='totalListen', blank=True, null=True)  # Field name made lowercase.
    id_song = models.OneToOneField(Song, models.DO_NOTHING, db_column='id_song', primary_key=True)

    class Meta:
        managed = False
        db_table = 'SongListenWeek'


class Topic(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Topic'


class Usersong(models.Model):
    id_user = models.ForeignKey('ApiUser', models.DO_NOTHING, db_column='id_user', to_field='username', blank=True, null=True)
    id_song = models.ForeignKey(Song, models.DO_NOTHING, db_column='id_song', blank=True, null=True)
    islike = models.BooleanField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    recenly_listen_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserSong'


class ApiUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_login = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    username = models.CharField(unique=True, max_length=100, blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    is_staff = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_user'


class ApiUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(ApiUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_user_groups'
        unique_together = (('user', 'group'),)


class ApiUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(ApiUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ApiUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
