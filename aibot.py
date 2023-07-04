from flask import Flask, jsonify, request
import mysql.connector

def create_app():
    app = Flask(__name__)
    
    @app.route('/api/ai', methods=['GET'])
    def ai_endpoint():
        query = request.args.get('query')
    
        mydb = mysql.connector.connect(
            host="cloud.mindsdb.com",
            user="nexinstudio@gmail.com",
            password="HEB#YT^GV6732fdvT",
            port="3306"
        )
    
        cursor = mydb.cursor()
        query_r = f'SELECT response FROM mindsdb.gpt_model WHERE author_username = "dulmina2" AND text = "{query}";'
        cursor.execute(query_r)
        result = cursor.fetchone()
        if result:
            response = result[0]
        else:
            response = "Sorry, I couldn't find a response for that."
    
        return jsonify({response})
    
app = create_app()

if __name__ == "__main__":
    app.run()

