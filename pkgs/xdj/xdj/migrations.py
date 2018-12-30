from django.db import migrations
def forwards(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return
    migrations.CreateModel()
    # Your migration code goes here

class Migration(migrations.Migration):
    dependencies = [
        "xdj.models.systems.languages"
        # Dependencies to other migrations
    ]
    operations = [
        migrations.RunPython(forwards),
    ]