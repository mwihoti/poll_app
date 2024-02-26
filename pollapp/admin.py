from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_txt"]}),
        ("Date information", {"fields": ["pub_date"]})
        
        ]
    inlines =  [ChoiceInline]
    list_display = ["question_txt", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_txt"]

admin.site.register(Question, QuestionAdmin)