import requests
import os

# Please make sure these variables are exported in the environment
# sp_client_id = os.environ['SP_CLIENT_ID']
# sp_client_secret = os.environ['SP_CLIENT_SECRET']
# tenant_id = os.environ['TENANT_ID']
# db_url = os.environ['DATABRICKS_HOST']

def get_aad_token(sp_client_id, sp_client_secret, tenant_id):
    # function returns AAD token. The default lifespan of the token is 599 seconds.
    data = {
        'client_id': sp_client_id,
        'grant_type': 'client_credentials',
        'scope': '2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default',
        'client_secret': sp_client_secret,
    }

    response = requests.post(f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token', data=data)
    aad_response = response.json()
    token = aad_response['access_token']
    return token


def gen_pat_for_sp(sp_client_id, sp_client_secret, tenant_id, db_url):
    # You can configure the lifetime_seconds parameter
    access_token = get_aad_token(sp_client_id, sp_client_secret, tenant_id)
    data = '{"comment": "pat for sp","lifetime_seconds": "10000"}'

    headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'text/plain',
    } 

    response = requests.post(f'{db_url}/api/2.0/token/create', headers=headers, data=data)

    response_json = response.json()
    pat_token = response_json['token_value']
    return pat_token
 