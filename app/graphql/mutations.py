import graphene

from app.models import collections, objects, inputs


class CreateRetrieveUser(graphene.Mutation):
    class Arguments:
        inputs = inputs.UserInputType(required=True)

    user = graphene.Field(objects.UserType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        if "keycloak_user_id" not in inputs:
            raise Exception("`keycloak_user_id` is required for this operation.")
        try:
            user = collections.User.objects(keycloak_user_id=inputs["keycloak_user_id"])
            if user.count() == 0:
                return CreateRetrieveUser(user=collections.User(**inputs).save())
            else:
                return CreateRetrieveUser(user=user[0])
        except Exception:
            raise Exception("An unexpected database occurred.")


class UpdateUser(graphene.Mutation):
    class Arguments:
        inputs = inputs.UserInputType(required=True)

    user = graphene.Field(objects.UserType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        if "keycloak_user_id" not in inputs:
            raise Exception("`keycloak_user_id` is required for this operation.")
        try:
            user = collections.User.objects(
                keycloak_user_id=inputs["keycloak_user_id"]
            )[0]
            user.modify(**inputs)
            return UpdateUser(user=user)
        except Exception:
            raise Exception("An unexpected database occurred.")


class DeleteUser(graphene.Mutation):
    class Arguments:
        inputs = inputs.UserInputType(required=True)

    user = graphene.Field(objects.UserType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        if "keycloak_user_id" not in inputs:
            raise Exception("`keycloak_user_id` is required for this operation.")
        try:
            user = collections.User.objects(
                keycloak_user_id=inputs["keycloak_user_id"]
            )[0]
            user.delete()
            return DeleteUser(user=user)
        except Exception:
            raise Exception("An unexpected database occurred.")


class Mutation(graphene.ObjectType):
    create_retrieve_user = CreateRetrieveUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
