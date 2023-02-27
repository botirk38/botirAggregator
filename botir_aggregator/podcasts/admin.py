from django.contrib import admin

# Register your models here.
from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("title", "podcast_name", "pub_date")
    list_filter = ("podcast_name", "pub_date")
    search_fields = ("title", "podcast_name")