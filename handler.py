from monitoring import api, crypto, webpage
from notifications import send_sms, send_email, send_to_slack


def run():
    # monitoring - uncomment the one you want to use
    msg = api.check_exchange_rate()
    # msg = crypto.check_available_mim()
    # msg = webpage.find_add_to_cart_button()

    # notification - uncomment the one you want to use
    if msg:
        # send_sms.send_sms(msg=msg)
        # send_email.send_email(msg=msg)
        send_to_slack.send_to_slack(msg=msg)
