from functools import wraps


from flask import current_app, request, Response
from flask_admin.contrib.sqla import ModelView



def check_auth(username, password):
    return all((username == current_app.config['USER_NAME'],
                password == current_app.config['PASSWORD']))


def authenticate(http_401_unauthorized=401):
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', http_401_unauthorized,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return func(*args, **kwargs)
    return decorated


class PizzaView(ModelView):
    @requires_auth
    def _handle_view(self, username, **kwargs):
        return super(PizzaView, self)._handle_view(username, **kwargs)
