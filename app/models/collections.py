from datetime import datetime

from mongoengine import (
    Document,
    EmbeddedDocument,
    UUIDField,
    StringField,
    DateField,
    IntField,
    BooleanField,
    ListField,
    ReferenceField,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
)


class EmploymentSection(EmbeddedDocument):
    id = UUIDField(required=True)
    title = StringField()
    employer = StringField()
    date_started = DateField()
    date_ended = DateField()
    location = StringField()
    description = StringField()


class EducationSection(EmbeddedDocument):
    id = UUIDField(required=True)
    degree = StringField()
    school = StringField()
    date_started = DateField()
    date_ended = DateField()
    location = StringField()


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
    keycloak_user_id = StringField(primary_key=True)
    full_name = StringField()
    profile = EmbeddedDocumentField(UserProfile)
    settings = EmbeddedDocumentField(UserSettings)
    is_premium = BooleanField(default=False)

    meta = {
        "indexes": [
            {"fields": ["$full_name", "$profile.major", "$profile.current_university"]}
        ]
    }


class FriendsRequest(Document):
    pairing = ListField(StringField(), required=True)
    status = StringField(required=True)
    seen = BooleanField(required=True, default=False)


class JobApplication(EmbeddedDocument):
    applicant = ReferenceField(User)
    date_graduated = DateField()
    date_start = DateField()
    reason = StringField()


class Job(Document):
    poster = ReferenceField(User)
    title = StringField()
    employer = StringField()
    location = StringField()
    salary = StringField()
    description = StringField()
    saved_by = ListField(ReferenceField(User))
    applications = EmbeddedDocumentListField(JobApplication)


class Message(Document):
    sender = ReferenceField(User)
    recipient = ReferenceField(User)
    category = StringField()
    message = StringField()
    sent_on = DateField(default=datetime.utcnow)
    seen = BooleanField(default=False)
