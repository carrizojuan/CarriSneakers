from django.core.exceptions import PermissionDenied

def superuser_required():
    def deco_permissions(f):
        def check(request, *args, **kwargs):
            if not request.user.is_superuser:
                raise PermissionDenied
            return f(request,*args, **kwargs)
        return check
    return deco_permissions