import firebase_admin
from firebase_admin import credentials, firestore
#from firebase import firebase 
import pyrebase
import sys, csv

cred = credentials.Certificate('/home/quangtong/Working/firebase_vtisandbox/hlc-mbe-firebase-adminsdk-tlxc4-05b69777b0.json')

app = firebase_admin.initialize_app(cred)
store = firestore.client()
doc_ref = store.collection(u'highland').document(u'environments').collection(u'development').document(u'catalog').collection(u'product_templates')
data = []

docs = doc_ref.get()

with open('hlcmbe_item.csv',mode='w') as test_file:
	writer = csv.writer(test_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['id','name','is_published','Type'])
	for doc in docs:
		doc_edit = doc.to_dict()
		if not 'name' in doc_edit:
			doc_edit['name'] = "N/A"
	
		if not 'is_published' in doc_edit:
			doc_edit['is_published'] = "N/A"
			ispub = "N/A"
		else:
			if type(doc_edit['is_published']) == bool:
				#ispub = str(doc_edit['is_published']) + " Boolean"
				ispub = "Boolean"
			else:
				#ispub = doc_edit['is_published'] + " String"
				ispub = "String"
		print (str(doc_edit['id']) + ' ' + str(doc_edit['name']) + ' ' + str(doc_edit['is_published'])) 
		#writer.writerow([doc_edit['id'],str(doc_edit['name']),str(doc_edit['is_published'])])
		writer.writerow([doc_edit['id'],str(doc_edit['name']),str(doc_edit['is_published']),ispub])
print('Done')