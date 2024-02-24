# Generated by Django 4.2.8 on 2024-02-19 06:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_alter_order_id_alter_order_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
                ("unit", models.CharField(default="บาทต่อถุง", max_length=100)),
                ("score", models.FloatField(blank=True, default=0, null=True)),
                (
                    "quantity_review",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="media/image/"),
                ),
                (
                    "options",
                    models.CharField(
                        choices=[
                            ("notchoose", "ไม่ได้เลือก"),
                            ("onsale", "วางขาย"),
                            ("soldout", "ขายหมดแล้ว"),
                        ],
                        default="notchoose",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Historysale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_field", models.DateField()),
                (
                    "food",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app.food",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reviewfood",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("review", models.TextField(blank=True, max_length=500, null=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "1 ดาว"),
                            (2, "2 ดาว"),
                            (3, "3 ดาว"),
                            (4, "4 ดาว"),
                            (5, "5 ดาว"),
                        ],
                        default=5,
                    ),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.food"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.userprofile",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="itemimage",
            name="item",
        ),
        migrations.AlterField(
            model_name="detailcart",
            name="itemImages",
            field=models.ImageField(blank=True, null=True, upload_to="media/image/"),
        ),
        migrations.DeleteModel(
            name="Item",
        ),
        migrations.DeleteModel(
            name="ItemImage",
        ),
    ]