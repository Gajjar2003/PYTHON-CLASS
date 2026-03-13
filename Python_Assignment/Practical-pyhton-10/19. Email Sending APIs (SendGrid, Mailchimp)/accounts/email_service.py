from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings

def send_confirmation_email(email, name):

    message = Mail(
        from_email=settings.FROM_EMAIL,
        to_emails=email,
        subject="Registration Successful",
        html_content=f"<h2>Hello {name}</h2><p>Your registration was successful.</p>"
    )

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        sg.send(message)
    except Exception as e:
        print(e)