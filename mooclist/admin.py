from django.contrib import admin
from .models import Department, Discipline, Course

#from django.contrib.auth.models import User
#from django.contrib.auth.admin import UserAdmin


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "discipline", "platform", "price", "available", "link_short", "weeks", "hours"
    list_display_links = "pk", "name"
    ordering = "pk",
    search_fields = "name", "platform"

    def link_short(
        self,
        obj: Course
    ) -> str:
        if len(obj.link) < 20:
            return obj.link
        return obj.link[:20] + "..."

    """def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.user != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.user != request.user:
            return False
        return True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.nam == "user":
            kwargs["queryset"] = User.objects.filter(
                username=request.user.username)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)"""

    """ def get_readonly_fields(self, request, obj=None):
            fields = list(super().get_readonly_fields(request))
            if not request.user.is_superuser:
                fields.append('name')
                return fields
    """

    """
    def get_queryset(self, request):
                    qs = super(ProjectAdmin, self).get_quesryset(request)
                    if request.user.is_superuser:
                        return qs
                    return qs.filter(department=request.user)
    """

    """
    def get_fieldsets(self, request, obj=None):
        if obj:
            if request.user.id == 1:
                return self.declared_fieldsets
            else:
                if obj.get_profile().type==1:
                    return (
                        (None, {'fields': ('username', 'password')}),
                        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                    )
                else:
                    return (
                        (None, {'fields': ('username', 'password')}),
                        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'user_permissions')}),
                        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                    )
        else:
            return self.add_fieldsets
            
    """

"""    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and request.user not in obj.department.all():
            return False
        return True"""


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = "pk", "name"

    """def get_readonly_fields(self, request, obj=None):
        fields = list(super().get_readonly_fields(request))
        if not request.user.is_superuser:
            fields.append('name')
            return fields"""

    """def has_module_permission(self, request):
        return False"""


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = "pk", "name"



"""

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    actions = [
        'activate_users',
    ]
    
    #отметить несколько пользователей как активных
    def activate_users(self, request, queryset):
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))
    activate_users.short_description = 'Activate Users' #type: ignore
    
    #скрыть activate_users от пользователей без разрешения на изменение, переопределим get_actions
    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('auth.change_user'):
            del actions['activate_users']
            return actions
            
"""