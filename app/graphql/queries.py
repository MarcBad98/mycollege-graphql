import graphene

from app.models import collections, objects


class Query(graphene.ObjectType):
    search_users = graphene.List(
        objects.UserType,
        search=graphene.String(),
    )
    get_friends_requests = graphene.List(
        objects.FriendsRequestType,
        keycloak_user_id=graphene.String(required=True),
    )
    get_friends = graphene.List(
        objects.FriendType,
        keycloak_user_id=graphene.String(required=True),
    )
    get_jobs = graphene.List(objects.JobType)
    get_messages = graphene.List(
        objects.MessageType,
        keycloak_user_id=graphene.String(required=True),
    )

    def resolve_search_users(self, info, search):
        # pylint: disable=no-member
        return collections.User.objects.search_text(search)

    def resolve_get_friends_requests(self, info, keycloak_user_id):
        # pylint: disable=no-member
        return collections.FriendsRequest.objects(pairing=keycloak_user_id)

    def resolve_get_friends(self, info, keycloak_user_id):
        # pylint: disable=no-member
        return collections.FriendsRequest.objects().aggregate(
            [
                {"$match": {"pairing": keycloak_user_id}},
                {"$unwind": "$pairing"},
                {"$match": {"pairing": {"$ne": keycloak_user_id}}},
                {
                    "$lookup": {
                        "from": "user",
                        "localField": "pairing",
                        "foreignField": "_id",
                        "as": "user",
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "user": {"$arrayElemAt": ["$user", 0]},
                        "status": 1,
                    }
                },
                {
                    "$project": {
                        "keycloak_user_id": "$user._id",
                        "full_name": "$user.full_name",
                        "major": "$user.profile.major",
                        "current_university": "$user.profile.current_university",
                        "status": 1,
                    }
                },
            ]
        )

    def resolve_get_jobs(self, info):
        # pylint: disable=no-member
        return collections.Job.objects()

    def resolve_get_messages(self, info, keycloak_user_id):
        # pylint: disable=no-member
        return collections.Message.objects(
            recipient=keycloak_user_id,
            category="message",
        )
