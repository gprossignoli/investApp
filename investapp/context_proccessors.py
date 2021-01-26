

def base_context(request):
    context_data = dict()
    context_data['user_already_logged'] = request.user.is_authenticated
    return context_data
