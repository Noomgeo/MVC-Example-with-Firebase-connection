def showAllView(list):
   print('In your db we have %i users. Here they are:' %len(list))
   for item in list:
      print(item.id, item.name(), item.phone)
def startView():
   print('\nMVC - the simplest example')
   print('Do you want to see everyone in my db?[y/n] or to add a new document?[a]')
def endView():
   print('Goodbye!')