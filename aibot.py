import telebot
import mindsdb_sdk

def capp():
    # connects to the default port (47334) on localhost 
    server = mindsdb_sdk.connect()
    
    server = mindsdb_sdk.connect('https://cloud.mindsdb.com', login='oemsjxs@bugfoo.com', password='HEB#YT^GV6732fdvT')
    project = server.get_project('mindsdb')
    def Ai(user):    
    
        query_r = f'SELECT response FROM mindsdb.gpt_modelj WHERE author_username = "dulmina1" AND text = "{user}";'
        query = project.query(query_r)
    
        res=query.fetch()
            
        return res
    
    
    
    
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
