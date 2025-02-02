from chalice import Blueprint

from chalicelib import _overrides
from chalicelib.blueprints import bp_authorizers
from chalicelib.utils import assist_helper

app = Blueprint(__name__)
_overrides.chalice_app(app)


@app.route('/v1/assist/credentials', methods=['GET'], authorizer=bp_authorizers.api_key_authorizer)
def get_assist_credentials(context):
    credentials = assist_helper.get_temporary_credentials()
    if "errors" in credentials:
        return credentials
    return {"data": credentials}
