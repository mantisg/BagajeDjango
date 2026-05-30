from rest_framework.permissions import BasePermission

class IsCreator(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.is_creator
        )
    
class IsCreatorOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return (
            request.user.is_authenticated
            and request.user.is_creator
        )
    
class IsCommentOwnerOrCreator(BasePermission):
    """
    Comment owner can edit/delete.
    Site creator can edit/delete any comment.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return (
            obj.author == request.user
            or request.user.is_creator
        )