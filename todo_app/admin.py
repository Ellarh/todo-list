from django.contrib import admin
from .models import TodoList


class TodoListAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'task_is_done')
    list_editable = ('task_is_done', )


admin.site.register(TodoList, TodoListAdmin)
