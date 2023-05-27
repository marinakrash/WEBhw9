from mongoengine import EmbeddedDocument, Document, ReferenceField
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Tag(EmbeddedDocument):
    name = ListField(StringField())

class Quote(Document):
    tags = EmbeddedDocumentField(Tag)
    author = ReferenceField(Author)
    quote = StringField()
