import graphene
from graphene_mongo import MongoengineObjectType

from app.models import collections


class MetaDataType(graphene.ObjectType):
    """ Assortment of arbitrary fields used as metadata. """

    # JobType
    user_is_poster = graphene.Boolean()
    user_is_applicant = graphene.Boolean()
    user_has_saved = graphene.Boolean()

    # UserType
    user_is_confirmed_friend = graphene.Boolean()
    user_is_pending_friend = graphene.Boolean()
    user_sent_friends_request = graphene.Boolean()


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

    metadata = graphene.Field(
        MetaDataType,
        keycloak_user_id=graphene.String(required=True),
    )

    def resolve_metadata(self, info, keycloak_user_id):
        # pylint: disable=no-member
        is_confirmed_friend = keycloak_user_id in self.friends
        is_pending_friend = (
            collections.Message.objects(
                sender=keycloak_user_id,
                recipient=self.keycloak_user_id,
                category="friends-request",
                resolved=False,
            ).count()
            == 1
        )
        sent_friends_request = (
            collections.Message.objects(
                sender=self.keycloak_user_id,
                recipient=keycloak_user_id,
                category="friends-request",
                resolved=False,
            ).count()
            == 1
        )
        return MetaDataType(
            user_is_confirmed_friend=is_confirmed_friend,
            user_is_pending_friend=is_pending_friend,
            user_sent_friends_request=sent_friends_request,
        )

    class Meta:
        model = collections.User


class MessageType(MongoengineObjectType):
    class Meta:
        model = collections.Message


class JobApplicationType(MongoengineObjectType):
    class Meta:
        model = collections.JobApplication


class JobType(MongoengineObjectType):

    metadata = graphene.Field(
        MetaDataType,
        keycloak_user_id=graphene.String(required=True),
    )

    def resolve_metadata(self, info, keycloak_user_id):
        # pylint: disable=no-member
        is_poster = keycloak_user_id == self.poster
        is_applicant = keycloak_user_id in [app.applicant for app in self.applications]
        has_saved = (
            collections.User.objects(
                keycloak_user_id=keycloak_user_id,
                jobs_saved=str(self.id),
            ).count()
            == 1
        )
        return MetaDataType(
            user_is_poster=is_poster,
            user_is_applicant=is_applicant,
            user_has_saved=has_saved,
        )

    class Meta:
        model = collections.Job


class CourseType(MongoengineObjectType):
    class Meta:
        model = collections.Course
