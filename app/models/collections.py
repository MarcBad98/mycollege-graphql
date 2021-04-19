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
    description = StringField()


class UserProfile(EmbeddedDocument):
    full_name = StringField()
    university = StringField()
    major = StringField()
    about = StringField()
    employment = EmbeddedDocumentListField(EmploymentSection)
    education = EmbeddedDocumentListField(EducationSection)


class UserSettings(EmbeddedDocument):
    subscription_email = BooleanField(default=False)
    subscription_sms = BooleanField(default=False)
    targeted_advertising = BooleanField(default=False)
    language = StringField(default="English")


class User(Document):
    keycloak_user_id = StringField(primary_key=True)
    is_plus_user = BooleanField(default=False)
    profile = EmbeddedDocumentField(UserProfile, default=lambda: UserProfile())
    settings = EmbeddedDocumentField(UserSettings, default=lambda: UserSettings())
    friends = ListField(StringField())
    jobs_saved = ListField(StringField())

    meta = {
        "indexes": [
            {"fields": ["$profile.full_name", "$profile.university", "$profile.major"]}
        ]
    }


class Message(Document):
    sent_on = DateField(default=datetime.utcnow)
    sender = StringField(required=True)
    recipient = StringField(required=True)
    category = StringField(choices=["friends-request", "message", "notification"])
    title = StringField()
    message = StringField()
    resolved = BooleanField(default=False)


class JobApplication(EmbeddedDocument):
    applied_on = DateField(default=datetime.utcnow)
    applicant = StringField(required=True)
    date_graduated = DateField()
    date_start = DateField()
    reason = StringField()


class Job(Document):
    posted_on = DateField(default=datetime.now)
    poster = StringField(required=True)
    title = StringField()
    employer = StringField()
    location = StringField()
    salary = StringField()
    description = StringField()
    applications = EmbeddedDocumentListField(JobApplication)
