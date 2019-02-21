from rest_framework.permissions import BasePermission

class IsAdder(BasePermission):
	message = "No, Please Stop!"
	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or obj.added_by == request.user:
			return True
		return False