from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently',)

    # Question.was_published_recently.boolean = True
    # Question.was_published_recently.ordering = 'pub_date'
    # Question.was_published_recently.description = 'Published recently?'

    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
