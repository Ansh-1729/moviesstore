from django.db import models

# Create your models here.
from django.shortcuts import render

# Create your views here.
# petitions/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=220, db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="petitions_created")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    def yes_count(self) -> int:
        return self.votes.count()

    def has_voted(self, user) -> bool:
        if not user or not user.is_authenticated:
            return False
        return self.votes.filter(user=user).exists()

    def save(self, *args, **kwargs):
        # Create a unique slug on first save, even if title collides
        if not self.slug:
            base = slugify(self.title)[:200] or "petition"
            candidate = base
            n = 1
            while Petition.objects.filter(slug=candidate).exists():
                n += 1
                candidate = f"{base}-{n}"
                if len(candidate) > 220:
                    candidate = candidate[:220]
            self.slug = candidate
        super().save(*args, **kwargs)


class Vote(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="petition_votes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["petition", "user"], name="unique_vote_per_user_per_petition")
        ]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user} → {self.petition}"
