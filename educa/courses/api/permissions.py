from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    """
    Ограничитель доступа для студентов, показ только курсов на которые юзер подписан
    """
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
