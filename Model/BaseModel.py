import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('ServiceKeyAPI.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def register_user(email, password):
    doc_ref = db.collection('user').document()
    doc_ref.set({
        "email": email,
        "password": password
    })


def login_user(email, password):
    doc_ref = db.collection('user').where('email','==', email).stream()
    for doc in doc_ref:
        if doc.to_dict()["email"] == email & doc.to_dict['password0'] == password:
            return "Login Successful"
        else:
            return "Try again"
