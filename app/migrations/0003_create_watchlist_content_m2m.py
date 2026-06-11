from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_add_watchlist_columns'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE TABLE IF NOT EXISTS "app_watchlist_content" (
                    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "watchlist_id" BIGINT NOT NULL REFERENCES "app_watchlist"("id") DEFERRABLE INITIALLY DEFERRED,
                    "audiovisualcontent_id" BIGINT NOT NULL REFERENCES "app_audiovisualcontent"("id") DEFERRABLE INITIALLY DEFERRED
                );
                CREATE INDEX IF NOT EXISTS "app_watchlist_content_audiovisualcontent_id" ON "app_watchlist_content" ("audiovisualcontent_id");
                CREATE UNIQUE INDEX IF NOT EXISTS "app_watchlist_content_watchlist_id_audiovisualcontent_id_uniq" ON "app_watchlist_content" ("watchlist_id", "audiovisualcontent_id");
            """,
            reverse_sql="""
                DROP TABLE IF EXISTS "app_watchlist_content";
            """,
        ),
    ]
