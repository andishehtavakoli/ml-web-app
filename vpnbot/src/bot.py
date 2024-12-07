import requests
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from dotenv import load_dotenv

load_dotenv()

# Get variables from the .env file
TELEGRAM_BOT_TOKEN = os.getenv("TOKEN")
HIDDIFY_API_KEY = os.getenv("HIDDIFY_API_KEY")
PROXY_PATH = os.getenv("PROXY_PATH")
BASE_URL = f"https://pypanell.pythoni.space/{PROXY_PATH}/api/v2/admin/user/"

# Function to fetch users from the API
def fetch_users():
    headers = {
        "Accept": "application/json",
        "Hiddify-API-Key": HIDDIFY_API_KEY,
    }
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code == 200:
        return response.json()  # Assuming the response is in JSON format
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = fetch_users()
    if not users:
        await update.message.reply_text("Failed to fetch user list.")
        return

    keyboard = [
        [InlineKeyboardButton(user["name"], callback_data=user["id"])]
        for user in users
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Select a user:", reply_markup=reply_markup)

# Callback query handler for user details
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the callback query
    user_id = query.data

    # Call API for user details
    headers = {
        "Accept": "application/json",
        "Hiddify-API-Key": HIDDIFY_API_KEY,
    }
    detail_url = f"{BASE_URL}{user_id}/"  # Adjust based on your API
    response = requests.get(detail_url, headers=headers)
    if response.status_code == 200:
        user_details = response.json()
        # Format and display user details
        details_text = (
            f"Name: {user_details['name']}\n"
            f"Usage (GB): {user_details['current_usage_GB']}\n"
            f"Last Online: {user_details['last_online']}\n"
            f"Package Days: {user_details['package_days']}\n"
            f"Usage Limit (GB): {user_details['usage_limit_GB']}\n"
            f"Active: {'Yes' if user_details['is_active'] else 'No'}"
        )
        await query.edit_message_text(details_text)
    else:
        await query.edit_message_text("Failed to fetch user details.")

# Main function to set up the bot
def main():
    # Create the Application object
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
