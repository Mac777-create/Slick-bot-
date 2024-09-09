from instagrapi import Client
import time

# Fonction de connexion sécurisée
def login_instagram(username, password):
    cl = Client()
    try:
        cl.login(username, password)
        print("Connexion réussie à Instagram.")
        return cl
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None

# Fonction pour aimer les posts en fonction de certains hashtags
def like_posts(cl, hashtags):
    for hashtag in hashtags:
        medias = cl.hashtag_medias_recent(hashtag)
        for media in medias:
            cl.media_like(media.id)
            print(f"Post aimé : {media.id}")
        time.sleep(60)  # Attendre une minute entre chaque like

# Fonction pour commenter automatiquement
def comment_on_posts(cl, hashtags, comment):
    for hashtag in hashtags:
        medias = cl.hashtag_medias_recent(hashtag)
        for media in medias:
            cl.media_comment(media.id, comment)
            print(f"Commentaire ajouté sur le post : {media.id}")
        time.sleep(60)

# Fonction pour automatiser les DM aux nouveaux abonnés
def send_dm_to_new_followers(cl, message):
    followers = cl.user_followers(cl.user_id)
    for follower in followers:
        cl.direct_send(message, [follower.pk])
        print(f"Message envoyé à {follower.username}")

# Fonction pour surveiller qui te suit ou se désabonne
def monitor_followers(cl):
    followers = cl.user_followers(cl.user_id)
    # Comparer avec une liste précédente d'abonnés pour détecter les désabonnements
    return followers

# Fonction pour publier du contenu programmé
def schedule_post(cl, image_path, caption):
    cl.photo_upload(image_path, caption)
    print("Publication effectuée.")
