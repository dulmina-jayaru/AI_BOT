import telebot
import mysql.connector

import mysql.connector
def Ai(query):
    mydb = mysql.connector.connect(
        host="cloud.mindsdb.com",
        user="oemsjxs@bugfoo.com",
        password="HEB#YT^GV6732fdvT",
        port="3306"
    )

    cursor = mydb.cursor()
    query_r = f'SELECT response FROM mindsdb.gpt_modelj WHERE author_username = "dulmina1" AND text = "{query}";'
    cursor.execute(query_r)
    result = cursor.fetchone()
    if result:
        response = result[0]
        
    else:
        print("Sorry, I couldn't find a response for that.")
        
    return response




TELEGRAM_BOT_TOKEN = '6060311779:AAF090Dt5lP5I_dZNPebK7HH6an8nPvU9iU'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    query = message.text
    # Pass the message to ChatGPT for generating a response
    bot.send_chat_action(chat_id=message.chat.id, action='typing')

    response = Ai(query)
    # Send the generated response back to the user
    bot.send_message(chat_id=message.chat.id, text=response)

bot.polling()
