# Generated by Django 4.1.5 on 2023-12-11 05:50

import colorful.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import modelcluster.contrib.taggit
import modelcluster.fields
import puput.routes
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("taggit", "0005_auto_20220424_2025"),
        ("wagtailcore", "0078_referenceindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        max_length=80, unique=True, verbose_name="Category name"
                    ),
                ),
                ("slug", models.SlugField(max_length=80, unique=True)),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=500, verbose_name="Description"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="puput.category",
                        verbose_name="Parent category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="CategoryEntryPage",
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
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="puput.category",
                        verbose_name="Category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EntryPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime.today, verbose_name="Post date"
                    ),
                ),
                (
                    "excerpt",
                    wagtail.fields.RichTextField(
                        blank=True,
                        help_text="Entry excerpt to be displayed on entries list. If this field is not filled, a truncate version of body text will be used.",
                        verbose_name="excerpt",
                    ),
                ),
                ("num_comments", models.IntegerField(default=0, editable=False)),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(
                                                class_name="heading-blog",
                                                max_length=255,
                                            ),
                                        )
                                    ]
                                ),
                            ),
                            ("paragraph", wagtail.blocks.CharBlock(max_length=255)),
                            (
                                "html",
                                wagtail.blocks.RawHTMLBlock(
                                    icon="code", label="Raw HTML"
                                ),
                            ),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                            (
                                "text_with_heading",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(max_length=255),
                                        ),
                                        ("text", wagtail.blocks.TextBlock()),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "text_with_heading_and_right_image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(
                                                class_name="heading-blog",
                                                max_length=255,
                                            ),
                                        ),
                                        ("text", wagtail.blocks.TextBlock()),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "text_with_heading_and_left_image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(
                                                class_name="blog", max_length=255
                                            ),
                                        ),
                                        ("text", wagtail.blocks.TextBlock()),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "right_image_left_text",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        ("text", wagtail.blocks.TextBlock()),
                                    ]
                                ),
                            ),
                            (
                                "left_image_right_text",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        ("text", wagtail.blocks.TextBlock()),
                                    ]
                                ),
                            ),
                            (
                                "left_quote_right_image",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("quote", wagtail.blocks.TextBlock()),
                                        (
                                            "byline",
                                            wagtail.blocks.CharBlock(max_length=255),
                                        ),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "video_embed",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(max_length=255),
                                        ),
                                        ("text", wagtail.blocks.TextBlock()),
                                    ]
                                ),
                            ),
                            ("table", wagtail.contrib.table_block.blocks.TableBlock()),
                            (
                                "code_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "language",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    ("Python", "python"),
                                                    ("Markup", "html"),
                                                    ("CSS", "css"),
                                                    ("Clojure", "clojure"),
                                                    ("Bash", "shell"),
                                                    ("Django", "django"),
                                                    ("Jinja2", "jinja2"),
                                                    ("Docker", "dockerfile"),
                                                    ("Git", "git"),
                                                    ("GraphQL", "graphql"),
                                                    ("Handlebars", "handlebars"),
                                                    (".ignore", "gitignore"),
                                                    ("JSON", "json"),
                                                    ("JSON5", "json5"),
                                                    ("Markdown", "md"),
                                                    ("Markdown", "md"),
                                                    ("React JSX", "jsx"),
                                                    ("React TSX", "tsx"),
                                                    ("SASS", "sass"),
                                                    ("SCSS", "scss"),
                                                    ("TypeScript", "ts"),
                                                    ("vim", "vim"),
                                                ]
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.CharBlock(
                                                blank=True, max_length=255
                                            ),
                                        ),
                                        (
                                            "page",
                                            wagtail.blocks.CharBlock(
                                                blank=True, max_length=255
                                            ),
                                        ),
                                        (
                                            "code",
                                            wagtail.blocks.TextBlock(
                                                blank=True, max_length=1000
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                        null=True,
                        use_json_field=True,
                        verbose_name="StreamField Body",
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True,
                        through="puput.CategoryEntryPage",
                        to="puput.category",
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Entry",
                "verbose_name_plural": "Entries",
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("taggit.tag",),
        ),
        migrations.CreateModel(
            name="TagEntryPage",
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
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entry_tags",
                        to="puput.entrypage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EntryPageRelated",
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
                (
                    "entrypage_from",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_entrypage_from",
                        to="puput.entrypage",
                        verbose_name="Entry",
                    ),
                ),
                (
                    "entrypage_to",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_entrypage_to",
                        to="puput.entrypage",
                        verbose_name="Entry",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="entrypage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="puput.TagEntryPage",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="categoryentrypage",
            name="page",
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entry_categories",
                to="puput.entrypage",
            ),
        ),
        migrations.CreateModel(
            name="BlogPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="The blog description that will appear under the title.",
                        max_length=255,
                        verbose_name="Description",
                    ),
                ),
                (
                    "main_color",
                    colorful.fields.RGBColorField(
                        default="#4D6AE0", verbose_name="Blog Main Color"
                    ),
                ),
                (
                    "display_comments",
                    models.BooleanField(default=False, verbose_name="Display comments"),
                ),
                (
                    "display_categories",
                    models.BooleanField(
                        default=True, verbose_name="Display categories"
                    ),
                ),
                (
                    "display_tags",
                    models.BooleanField(default=True, verbose_name="Display tags"),
                ),
                (
                    "display_popular_entries",
                    models.BooleanField(
                        default=True, verbose_name="Display popular entries"
                    ),
                ),
                (
                    "display_last_entries",
                    models.BooleanField(
                        default=True, verbose_name="Display last entries"
                    ),
                ),
                (
                    "display_archive",
                    models.BooleanField(default=True, verbose_name="Display archive"),
                ),
                ("disqus_api_secret", models.TextField(blank=True)),
                ("disqus_shortname", models.CharField(blank=True, max_length=128)),
                (
                    "num_entries_page",
                    models.IntegerField(default=5, verbose_name="Entries per page"),
                ),
                (
                    "num_last_entries",
                    models.IntegerField(default=3, verbose_name="Last entries limit"),
                ),
                (
                    "num_popular_entries",
                    models.IntegerField(
                        default=3, verbose_name="Popular entries limit"
                    ),
                ),
                (
                    "num_tags_entry_header",
                    models.IntegerField(
                        default=5, verbose_name="Tags limit entry header"
                    ),
                ),
                (
                    "short_feed_description",
                    models.BooleanField(
                        default=True, verbose_name="Use short description in feeds"
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog",
            },
            bases=(puput.routes.BlogRoutes, "wagtailcore.page", models.Model),
            managers=[
                ("extra", django.db.models.manager.Manager()),
            ],
        ),
    ]