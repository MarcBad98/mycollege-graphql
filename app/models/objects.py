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


class FriendsRequestType(MongoengineObjectType):
    class Meta:
        model = collections.FriendsRequest
