import graphene
from graphene_mongo import MongoengineObjectType

from app.models import collections


class EmploymentSectionType(MongoengineObjectType):
    class Meta:
        model = collections.EmploymentSection


class EducationSectionType(MongoengineObjectType):
    class Meta:
        model = collections.EducationSection


class UserProfileType(MongoengineObjectType):
    class Meta:
        model = collections.UserProfile


class UserSettingsType(MongoengineObjectType):
    class Meta:
        model = collections.UserSettings


class UserType(MongoengineObjectType):
    class Meta:
        model = collections.User


class MessageType(MongoengineObjectType):
    class Meta:
        model = collections.Message


class JobApplicationType(MongoengineObjectType):
    class Meta:
        model = collections.JobApplication


class JobType(MongoengineObjectType):
    class Meta:
        model = collections.Job
