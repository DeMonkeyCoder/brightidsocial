import requests


def is_user_app_id_linked(network, app_id, user_app_id):
    verification_url = f'http://{network}.brightid.org/brightid/' \
                       f'v6/verifications/{app_id}/{user_app_id}'
    return requests.get(verification_url).json()
