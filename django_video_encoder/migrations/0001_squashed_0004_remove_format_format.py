# Generated by Django 2.2.16 on 2020-10-29 16:19

import django.db.models.deletion
from django.db import migrations, models

import django_video_encoder.models


class Migration(migrations.Migration):

    replaces = [
        ("django_video_encoder", "0001_initial"),
        ("django_video_encoder", "0002_auto_20201022_1647"),
        ("django_video_encoder", "0003_auto_20201029_1613"),
        ("django_video_encoder", "0004_remove_format_format"),
    ]

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Thumbnail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("time", models.PositiveIntegerField(verbose_name="Time (s)")),
                ("width", models.PositiveIntegerField(null=True, verbose_name="Width")),
                (
                    "height",
                    models.PositiveIntegerField(null=True, verbose_name="Height"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        max_length=512,
                        null=True,
                        upload_to=django_video_encoder.models.thumbnail_upload_to,
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Format",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("field_name", models.CharField(max_length=255)),
                (
                    "file",
                    models.FileField(
                        max_length=2048,
                        upload_to=django_video_encoder.models.format_upload_to,
                    ),
                ),
                ("width", models.PositiveIntegerField(null=True, verbose_name="Width")),
                (
                    "height",
                    models.PositiveIntegerField(null=True, verbose_name="Height"),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        null=True, verbose_name="Duration (ms)"
                    ),
                ),
                (
                    "extra_info",
                    models.TextField(
                        blank=True, verbose_name="Encoder information (JSON)"
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "format_label",
                    models.CharField(default="", editable=False, max_length=80),
                ),
                (
                    "video_codec",
                    models.CharField(
                        choices=[
                            ("h264", "h264"),
                            ("hevc", "hevc"),
                            ("jp2", "jp2"),
                            ("mpeg4", "mpeg4"),
                            ("theora", "theora"),
                            ("vp6", "vp6"),
                            ("vp8", "vp8"),
                            ("vp9", "vp9"),
                            ("wmv", "wmv"),
                        ],
                        default="h264",
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
