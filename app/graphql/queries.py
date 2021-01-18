import graphene

from app.models import collections, objects


class Query(graphene.ObjectType):
    test = graphene.Field(objects.TestObjectType)

    def resolve_test(self, info):
        return objects.TestObjectType(
            test1="Test Successful!",
            test2=True,
            test3=9.8,
        )
