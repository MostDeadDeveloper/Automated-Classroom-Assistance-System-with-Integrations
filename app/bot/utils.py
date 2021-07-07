import requests

def fetch_login_data(discord_id):
    response = requests.post(
        'http://superepicguysuper.pythonanywhere.com/accounts/discord-auth',
        data={'discord_id': discord_id},
    )

    return response.content




