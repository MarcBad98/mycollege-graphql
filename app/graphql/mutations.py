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


class CreateJob(graphene.Mutation):
    class Arguments:
        inputs = inputs.JobInputType(required=True)

    job = graphene.Field(objects.JobType)

    def mutate(self, info, inputs):
        try:
            job = collections.Job(**inputs).save()
            return CreateJob(job=job)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class UpdateJob(graphene.Mutation):
    class Arguments:
        inputs = inputs.JobInputType(required=True)

    job = graphene.Field(objects.JobType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        if "id" not in inputs:
            raise Exception("`id` is required for this operation.")
        try:
            job = collections.Job.objects(id=inputs["id"])[0]
            job.modify(**inputs)
            return UpdateJob(job=job)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class DeleteJob(graphene.Mutation):
    class Arguments:
        inputs = inputs.JobInputType(required=True)

    job = graphene.Field(objects.JobType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        if "id" not in inputs:
            raise Exception("`id` is required for this operation.")
        try:
            job = collections.Job.objects(id=inputs["id"])[0]
            job.delete()
            return DeleteJob(job=job)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class ToggleSaveJob(graphene.Mutation):
    class Arguments:
        is_save = graphene.Boolean(required=True)
        keycloak_user_id = graphene.String(required=True)
        job_id = graphene.String(required=True)

    job = graphene.Field(objects.JobType)

    def mutate(self, info, is_save, keycloak_user_id, job_id):
        # pylint: disable=no-member
        try:
            user = collections.User.objects(keycloak_user_id=keycloak_user_id)[0]
            job = collections.Job.objects(id=job_id)[0]
            if is_save:
                job.modify(push__saved_by=user)
            else:
                job.modify(pull__saved_by=user)
            return ToggleSaveJob(job=job)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class SendJobApplication(graphene.Mutation):
    class Arguments:
        inputs = inputs.JobApplicationInputType(required=True)
        job_id = graphene.String(required=True)

    job = graphene.Field(objects.JobType)

    def mutate(self, info, inputs, job_id):
        # pylint: disable=no-member
        try:
            job = collections.Job.objects(id=job_id)[0]
            job.modify(push__applications=inputs)
            return SendJobApplication(job=job)
        except Exception:
            raise Exception("An unexpected database error occurred.")


class SendMessage(graphene.Mutation):
    class Arguments:
        inputs = inputs.MessageInputType(required=True)

    message = graphene.Field(objects.MessageType)

    def mutate(self, info, inputs):
        inputs["category"] = "message"
        try:
            message = collections.Message(**inputs).save()
            return SendMessage(message=message)
        except Exception:
            raise Exception("An unexpected database error ocurred.")


class ViewMessage(graphene.Mutation):
    class Arguments:
        message_id = graphene.String()

    success = graphene.Boolean()

    def mutate(self, info, message_id):
        # pylint: disable=no-member
        try:
            message = collections.Message.objects(id=message_id)[0]
            message.seen = True
            message.save()
            return ViewMessage(success=True)
        except Exception:
            raise Exception("An unexpected database error ocurred.")


class DeleteMessage(graphene.Mutation):
    class Arguments:
        inputs = inputs.MessageInputType(required=True)

    message = graphene.Field(objects.MessageType)

    def mutate(self, info, inputs):
        # pylint: disable=no-member
        if "id" not in inputs:
            raise Exception("`id` is required for this operation.")
        try:
            message = collections.Message.objects(id=inputs["id"])[0]
            message.delete()
            return DeleteMessage(message=message)
        except Exception:
            raise Exception("An unexpected database error ocurred.")


class Mutation(graphene.ObjectType):
    create_retrieve_user = CreateRetrieveUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_friends_request = CreateFriendsRequest.Field()
    update_friends_request = UpdateFriendsRequest.Field()
    delete_friends_request = DeleteFriendsRequest.Field()
    create_job = CreateJob.Field()
    update_job = UpdateJob.Field()
    delete_job = DeleteJob.Field()
    toggle_save_job = ToggleSaveJob.Field()
    send_job_application = SendJobApplication.Field()
    send_message = SendMessage.Field()
    view_message = ViewMessage.Field()
    delete_message = DeleteMessage.Field()
