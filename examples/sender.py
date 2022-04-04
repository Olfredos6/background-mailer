'''
    Used to interface with the BKG_MAILER API.
    Author: Nehemie 'Alfred' Balukidi
    Source at https://github.com/Olfredos6/background-mailer
    Exmaple:
        from athassanz.bkg_mailer import send_mail as send; 
        print(send("Hello!", ["recepient@email.com"], "Hello World!"))'
'''

import requests
from os import getenv


DEFAULT_MAIL_CONFIG = {
    'host': getenv('MAIL_HOST'),
    'port': getenv('MAIL_PORT'),
    'username': getenv('MAIL_USERNAME'),
    'password': getenv('MAIL_PASSWORD'),
    'html': True
}


def build_email_body(body: str, page_title: str = "Yoursite.com") -> str:
    # Returns the HTML string to be sent
    return f'''
        <!doctype html>
        <html lang="en">
        <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta
            name="viewport"
            content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link
            href="https://cdn.jsdelivr.net/npm/
            bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU
            8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">

            <title>{page_title}</title>
            <style>
            .card {{
                top: 2rem;
                /* border-color: #991916; */
                border: 0px solid;
            }}
            .card-title {{
                background-color: #991916;
                padding: 2rem;
                color: #fff/*#991916*/;
            }}
            .card-body {{
                flex: 1 1 auto;
                padding: 1rem 1rem;
            }}
            .card-footer {{
                bottom: 0px;
                background-color: unset;
                color: #133e72;
                margin-bottom: 0px;
                border-top: 1px solid #133e72;
            }}
            </style>
        </head>
        <body>
            <div
            class="card mx-auto"
            style="width: 70%; margin: auto"
            >
        <div class="card-title">
            <h5 >{page_title}</h5>
        </div>
        <div class="card-body">
                    {body}
        </div>
        <div class="card-footer">
            <p>{page_title}<br>
                    Copyright @ 2022</p>
        </div>
            </div>
            <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstra
            p.bundle.min.js"
            integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+
            OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
            crossorigin="anonymous"
            ></script>
        </body>
        </html>
        '''


def send_mail(subject: str, recipient: list, body) -> None:
    '''
        Tries to send a request to send an email to
        BKG-Emailer and returns a dictionary containing
        status code, text, and json.
    '''
    email_body = build_email_body(body)
    res = requests.post(
        getenv('BKG_MAILER_URL'),
        data={
            **DEFAULT_MAIL_CONFIG,
            'subject': subject,
            'recipient': recipient,
            'message': email_body
        }
    )

    return {
        'status': res.status_code,
        'text': res.content.decode("utf-8"),
        'json': res.json()
    }
