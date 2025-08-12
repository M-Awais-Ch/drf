from rest_framework.permissions import IsAdminUser
class MyPermission(IsAdminUser):
    def has_permission(self, request, view):
        if request.method=='POST':
            return True
        elif request.method == 'GET':
            return True
        elif request.method == 'DELETE':
            return True
        elif request.method == 'PUT':
            return True
        return False

