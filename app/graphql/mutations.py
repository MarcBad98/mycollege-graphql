import graphene

from app.models import collections, objects, inputs


###################################################################################################


class UserBaseMutation(graphene.Mutation):
    class Arguments:
        inputs = inputs.UserInputType(required=True)

    user = graphene.Field(objects.UserType)

    def mutate(self, info, inputs):
        pass


class CreateRetrieveUser(UserBaseMutation):
    def mutate(self, info, inputs):
        # pylint: disable=no-member
        user = collections.User.objects(keycloak_user_id=inputs["keycloak_user_id"])
        if user.count() == 0:
            user = collections.User(**inputs)
            user.save()
            return CreateRetrieveUser(user=user)
        else:
            return CreateRetrieveUser(user=user[0])


class UpdateUser(UserBaseMutation):
    def mutate(self, info, inputs):
        # pylint: disable=no-member
        user = collections.User.objects(keycloak_user_id=inputs["keycloak_user_id"])[0]
        user.modify(**inputs)
        return UpdateUser(user=user)


class DeleteUser(UserBaseMutation):
    def mutate(self, info, inputs):
        # pylint: disable=no-member
        user = collections.User.objects(keycloak_user_id=inputs["keycloak_user_id"])[0]
        user.delete()
        return DeleteUser(user=user)


###################################################################################################


class MessageBaseMutation(graphene.Mutation):
    class Arguments:
        inputs = inputs.MessageInputType(required=True)

    message = graphene.Field(objects.MessageType)

    def mutate(self, info, inputs):
        pass


class CreateMessage(MessageBaseMutation):
    def mutate(self, info, inputs):
        message = collections.Message(**inputs)
        message.save()
        return CreateMessage(message=message)


class UpdateMessage(MessageBaseMutation):
    def mutate(self, info, inputs):
        # pylint: disable=no-member
        message = collections.Message.objects(id=inputs["id"])[0]
        message.modify(**inputs)
        return UpdateMessage(message=message)


class DeleteMessage(MessageBaseMutation):
    def mutate(self, info, inputs):
        # pylint: disable=no-member
        message = collections.Message.objects(id=inputs["id"])[0]
        message.delete()
        return DeleteMessage(message=message)


###################################################################################################


class JobBaseMutation(graphene.Mutation):
    class Arguments:
        inputs = inputs.JobInputType(required=True)

    job = graphene.Field(objects.JobType)

    def mutate(self, info, inputs):
        pass


class CreateJob(JobBaseMutation):
    def mutate(self, info, inputs):
        job = collections.Job(**inputs)
        job.save()
        return CreateJob(job=job)


class UpdateJob(JobBaseMutation):
    def mutate(self, info, inputs):
        # pylint: disable=no-member
        job = collections.Job.objects(id=inputs["id"])[0]
        job.modify(**inputs)
        return UpdateJob(job=job)


class DeleteJob(JobBaseMutation):
    def mutate(self, info, inputs):
        # pylint: disable=no-member
        job = collections.Job.objects(id=inputs["id"])[0]
        job.delete()
        return DeleteJob(job=job)


###################################################################################################


class Mutation(graphene.ObjectType):
    create_retrieve_user = CreateRetrieveUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_message = CreateMessage.Field()
    update_message = UpdateMessage.Field()
    delete_message = DeleteMessage.Field()
    create_job = CreateJob.Field()
    update_job = UpdateJob.Field()
    delete_job = DeleteJob.Field()
