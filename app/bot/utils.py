import requests

def fetch_login_data(discord_id):
    print('Your Discord ID: {}'.format(discord_id))
    response = requests.post(
        'http://superepicguysuper.pythonanywhere.com/api/accounts/discord-auth',
        data={'discord_id': discord_id},
    )
    # returns account_id, token, status
    return response




