from django.contrib import admin
from .models import Student
# Register your models here.

admin.site.register(Student)
'''
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'course')
    search_fields = ('name', 'course')
    list_filter = ('course',)
    ordering = ('name',)
    '''
    