from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    BooleanField,
    EmbeddedDocumentField,
)


# class UserProfile(EmbeddedDocument):
#     pass


class UserSettings(EmbeddedDocument):
    subscription_email = BooleanField(default=False)
    subscription_sms = BooleanField(default=False)
    targeted_advertising = BooleanField(default=False)
    language = StringField(default="English")


class User(Document):
    keycloak_user_id = StringField()
    # profile =
    settings = EmbeddedDocumentField(UserSettings)
