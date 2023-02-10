import stripe
from flask import Flask, redirect
app = Flask(__name__)
stripe.api_key = "Rr6jkD....."  # your own purchased api key
domain = "http://localhost:5000"

@app.route('/paynow', methods=["POST"])
def paynow():
    try:
        payment_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": "{{product id/key}}", #    params['from json file also']
                    "quantity": 1
                }
            ],
            mode="subscription", # or One Time, in Subscription , Duration must select i.e. 1.Weekly, 2.Monthly, 3. 3 months
            success_url =   domain + "/pay_succesful.html",
            cancel_url  =   domain + "/pay_canceled.html"
        )
    except Exception as ex:
        return str(ex)

    return redirect(payment_session.url)

if __name__ == "__main__":
    app.run(debug=True)