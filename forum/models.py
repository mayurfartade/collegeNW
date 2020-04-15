# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Forum(models.Model):
    forum_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    forum_name = models.CharField(max_length=200)
    tags = models.CharField(max_length=48)
    description = models.TextField()
    reply = models.IntegerField()
    status = models.IntegerField()
    date_post = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'forum'


class ForumReplies(models.Model):
    reply_id = models.AutoField(primary_key=True)
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    reply = models.CharField(max_length=200)
    status = models.IntegerField(blank=True, null=True)
    posted_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'forum_replies'


class QuestionPapers(models.Model):
    que_id = models.AutoField(primary_key=True)
    subject_id = models.IntegerField(blank=True, null=True)
    que_year = models.IntegerField()
    link = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'question_papers'


class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=30)
    mobile = models.CharField(unique=True, max_length=10)
    gender = models.CharField(max_length=10)
    branch = models.IntegerField()
    year = models.IntegerField()
    div_field = models.CharField(db_column='div_', max_length=1)  # Field renamed because it ended with '_'.
    roll_no = models.IntegerField()
    prn_no = models.IntegerField()
    birthday = models.DateField()

    class Meta:
        managed = False
        db_table = 'student'


class Subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=40)
    sem = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subjects'
