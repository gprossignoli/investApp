import datetime


def base_context(request):
    context_data = dict()
    context_data['user_already_logged'] = request.user.is_authenticated
    context_data['time_stamp'] = datetime.datetime.today()
    return context_data
