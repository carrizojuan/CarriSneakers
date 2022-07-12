from django.core.exceptions import PermissionDenied


class SuperUserRequiredMixin():
    # permisos_requeridos = []
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)