import graphene

from app.models import collections, objects, inputs


class CreateRetrieveUser(graphene.Mutation):
    class Arguments:
        inputs = inputs.UserInputType(required=True)

    user = graphene.Field(objects.UserType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        try:
            user = collections.User.objects(keycloak_user_id=inputs["keycloak_user_id"])
            if user.count() == 0:
                return CreateRetrieveUser(user=collections.User(**inputs).save())
            else:
                return CreateRetrieveUser(user=user[0])
        except Exception:
            raise Exception("An unexpected database error occurred.")


class UpdateUser(graphene.Mutation):
    class Arguments:
        inputs = inputs.UserInputType(required=True)

    user = graphene.Field(objects.UserType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        try:
            user = collections.User.objects(
                keycloak_user_id=inputs["keycloak_user_id"]
            )[0]
            user.modify(**inputs)
            return UpdateUser(user=user)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class DeleteUser(graphene.Mutation):
    class Arguments:
        inputs = inputs.UserInputType(required=True)

    user = graphene.Field(objects.UserType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        try:
            user = collections.User.objects(
                keycloak_user_id=inputs["keycloak_user_id"]
            )[0]
            user.delete()
            return DeleteUser(user=user)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class CreateFriendsRequest(graphene.Mutation):
    class Arguments:
        inputs = inputs.FriendsRequestInputType(required=True)

    friends_request = graphene.Field(objects.FriendsRequestType)

    def mutate(self, info, inputs):
        if len(inputs["pairing"]) != 2:
            raise Exception("`pairing` must contain exactly 2 user ID values.")
        try:
            friends_request = collections.FriendsRequest(**inputs).save()
            return CreateFriendsRequest(friends_request=friends_request)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class UpdateFriendsRequest(graphene.Mutation):
    class Arguments:
        inputs = inputs.FriendsRequestInputType(required=True)

    friends_request = graphene.Field(objects.FriendsRequestType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        if len(inputs["pairing"]) != 2:
            raise Exception("`pairing` must contain exactly 2 user ID values.")
        try:
            friends_request = collections.FriendsRequest.objects(
                pairing=inputs["pairing"]
            )[0]
            friends_request.modify(**inputs)
            return UpdateFriendsRequest(friends_request=friends_request)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class DeleteFriendsRequest(graphene.Mutation):
    class Arguments:
        inputs = inputs.FriendsRequestInputType(required=True)

    friends_request = graphene.Field(objects.FriendsRequestType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        if len(inputs["pairing"]) != 2:
            raise Exception("`pairing` must contain exactly 2 user ID values.")
        try:
            friends_request = collections.FriendsRequest.objects(
                pairing=inputs["pairing"]
            )[0]
            friends_request.delete()
            return DeleteFriendsRequest(friends_request=friends_request)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class Mutation(graphene.ObjectType):
    create_retrieve_user = CreateRetrieveUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_friends_request = CreateFriendsRequest.Field()
    update_friends_request = UpdateFriendsRequest.Field()
    delete_friends_request = DeleteFriendsRequest.Field()
