from flask import Flask, request, render_template
from bot import login_instagram, like_posts, comment_on_posts, send_dm_to_new_followers, schedule_post

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    client = login_instagram(username, password)

    if client:
        return "Connexion réussie !"
    else:
        return "Échec de la connexion."

@app.route('/actions', methods=['POST'])
def perform_actions():
    # Exemple d'actions à exécuter après connexion
    hashtags = request.form['hashtags'].split(',')
    comment = request.form['comment']
    
    like_posts(client, hashtags)
    comment_on_posts(client, hashtags, comment)
    return "Actions effectuées."

if __name__ == "__main__":
    app.run(debug=True)
