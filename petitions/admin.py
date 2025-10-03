from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Petition, Vote

@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "yes_count")
    search_fields = ("title", "description", "created_by__username")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("petition", "user", "created_at")
    search_fields = ("petition__title", "user__username")
    readonly_fields = ("created_at",)