import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("noam-mvc-test-firebase-adminsdk-7wgs6-f7d5d2cf93.json")
firebase_admin.initialize_app(cred, {
  'projectId': 'noam-mvc-test',
})

db = firestore.client()

# Then query for documents
person_ref = db.collection(u'person')
docs = person_ref.get()

for doc in docs:
    #print(u'{} => {}'.format(doc.id, doc.to_dict()))
    person = doc.to_dict()
    print(person['first_name'], person['last_name'], person['phone'])