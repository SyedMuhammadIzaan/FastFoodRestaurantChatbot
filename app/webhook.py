from flask import Blueprint, request, jsonify

from app.services.menu import getAllMenu
from prompts import ask_gemini

webhook_bp = Blueprint("webhook", __name__)


@webhook_bp.route("/webhook", methods=["POST"])
def handle_webhook():

    data = request.get_json()
    # print("Webhook data received:", data)

    query_result = data.get("queryResult", {})

    # Get intent name
    intent = query_result.get("intent", {}).get("displayName")

    # print("Intent:", intent)

    # Greeting
    if intent == "Welcome":

        question=query_result.get("queryText", "")
        answer=ask_gemini(question)
        print("Answer:", answer)
        return jsonify({
            "fullfillmentText": answer
    })

    # Menu
    elif intent == "Menu":

        menus = getAllMenu()
        print("Menus:", menus)
        if not menus:
            response = "Sorry, our menu is currently empty."

        else:
            response = "Here is our menu:\n"
            response += "-------------------------\n\n"

            for menu in menus:
                response += (
                    f"{menu['name']} - \n"
                    f"{menu['description']} -\n "
                    f"Rs. {menu['price']}\n"
                )

    # Unknown intent
    else:

        response = "Sorry, I don't understand your request."

    return jsonify({
        "fulfillmentText": response
    })