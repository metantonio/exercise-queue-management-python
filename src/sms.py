# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACc631797a42a40487ea82d89e493766c9'
    auth_token = 'b28b3bb977cf807e28df632d3a3f18a8'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+14703975037',  #+13346058062
                        to='+'+to
                    )

    print(message.sid)