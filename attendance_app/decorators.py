
from django.shortcuts import redirect

def unauthenticated_user_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('user_profile/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

