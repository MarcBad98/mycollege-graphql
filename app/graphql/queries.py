import graphene

from app.models import collections, objects, inputs


class Query(graphene.ObjectType):
    search_users = graphene.List(
        objects.UserType,
        search=graphene.String(required=True),
    )
    get_messages = graphene.List(
        objects.MessageType,
        inputs=inputs.MessageInputType(),
    )
    get_jobs = graphene.List(
        objects.JobType,
        inputs=inputs.JobInputType(),
    )

    def resolve_search_users(self, info, search):
        # pylint: disable=no-member
        return collections.User.objects.search_text(search)

    def resolve_get_messages(self, info, inputs=None):
        # pylint: disable=no-member
        if inputs is None:
            inputs = {}
        return collections.Message.objects(**inputs)

    def resolve_get_jobs(self, info, inputs=None):
        # pylint: disable=no-member
        if inputs is None:
            inputs = {}
        return collections.Job.objects(**inputs)
