from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from bookwormsunite.forms import ReaderCreationForm
from bookwormsunite.models import Reader, Readathon, Challenge, Accomplishment, Book, Activity


@admin.register(Reader)
class ReaderAdmin(UserAdmin):
    form = UserChangeForm
    add_form = ReaderCreationForm

    list_display = ('username', 'is_superuser', 'is_active', 'img',)
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Information', {'fields': ('img',)}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password2')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


@admin.register(Readathon)
class ReadathonAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'start_date', 'end_date',)


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


@admin.register(Accomplishment)
class AccomplishmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'isbn', 'author',)


admin.site.register(Activity)
