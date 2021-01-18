import graphene


class TestObjectType(graphene.ObjectType):
    test1 = graphene.String()
    test2 = graphene.Boolean()
    test3 = graphene.Float()
