class Person:
    pass

person = Person()

class Members:
    pass
members = Members()

print(person)
print(members)
print(isinstance(members, Person))
print(isinstance(members, Members))

# Class Varaibles

class Document:
    language = 'Python'
    version = 1.23
    def helloWorld():
        print("Hello world!")

a = Document.language
print(a)
Document.version = 2.69
b = Document.language
print(b)

getAtt = getattr(Document, 'language')
getAtt1 = getattr(Document, 'version')
print(getAtt, getAtt1)

Document.media = 'mp4'
getAtt2 = getattr(Document, 'media')
setattr(Document, 'Device', 'Laptop')
getAtt3 = getattr(Document, 'Device')
print(getAtt2, getAtt3)

print(Document.__dict__)

