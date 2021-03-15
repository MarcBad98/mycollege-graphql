import graphene

from app.models import collections, objects


class Query(graphene.ObjectType):
    search_users = graphene.List(
        objects.UserType,
        search=graphene.String(),
    )
    get_friend_requests = graphene.List(
        objects.FriendsRequestType,
        keycloak_user_id=graphene.String(required=True),
    )
    get_friends = graphene.List(
        objects.UserType,
        keycloak_user_id=graphene.String(required=True),
    )

    def resolve_search_users(self, info, search):
        # pylint: disable=no-member
        return collections.User.objects.search_text(search)

    def resolve_get_friend_requests(self, info, keycloak_user_id):
        # pylint: disable=no-member
        return collections.FriendsRequest.objects(pairing=keycloak_user_id)

    def resolve_get_friends(self, info, keycloak_user_id):
        # pylint: disable=no-member
        results = collections.FriendsRequest.objects().aggregate(
            [
                {"$match": {"pairing": keycloak_user_id, "status": "ACCEPTED"}},
                {"$unwind": "$pairing"},
                {"$match": {"pairing": {"$ne": keycloak_user_id}}},
                {"$project": {"_id": 0, "keycloak_user_id": "$pairing"}},
            ]
        )
        return collections.User.objects(
            keycloak_user_id__in=[result["keycloak_user_id"] for result in results]
        )
