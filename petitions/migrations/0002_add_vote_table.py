from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('petition', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='votes', to='petitions.petition')),
                ('user', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='petition_votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=['petition', 'user'], name='unique_vote_per_user_per_petition'),
        ),
    ]