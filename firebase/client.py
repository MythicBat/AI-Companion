import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate("firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_mood(user: str, mood: int, date: str):
    doc_ref = db.collection("mood_entries").document(user + "_" + date)
    doc_ref.set({
        "user": user,
        "mood": mood,
        "date": date
    })

def get_mood_history(user: str):
    """
    Fetch all mood entries for a user from Firestore
    Returns a list of (date, mood) tuples sorted by date.
    """
    moods = db.collection("mood_entries").where("user", "==", user).stream()
    entries = []

    for doc in moods:
        data = doc.to_dict()
        entries.append((data["date"], data["mood"]))

    # Sort by date
    entries.sort()
    return entries