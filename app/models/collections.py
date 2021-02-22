from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    DateField,
    IntField,
    BooleanField,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
)


class EmploymentSection(EmbeddedDocument):
    title = StringField()
    employer = StringField()
    date_started = DateField()
    date_ended = DateField()
    location = StringField()
    description = StringField()


class EducationSection(EmbeddedDocument):
    degree = StringField()
    school = StringField()
    date_started = DateField()
    date_ended = DateField()
    location = StringField()
    years_attended = IntField()


class UserProfile(EmbeddedDocument):
    title = StringField()
    major = StringField()
    current_university = StringField()
    about = StringField()
    employment = EmbeddedDocumentListField(EmploymentSection)
    education = EmbeddedDocumentListField(EducationSection)


class UserSettings(EmbeddedDocument):
    subscription_email = BooleanField()
    subscription_sms = BooleanField()
    targeted_advertising = BooleanField()
    language = StringField()


class User(Document):
    keycloak_user_id = StringField()
    full_name = StringField()
    profile = EmbeddedDocumentField(UserProfile)
    settings = EmbeddedDocumentField(UserSettings)
