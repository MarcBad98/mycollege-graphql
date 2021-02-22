import graphene


class EmploymentSectionInputType(graphene.InputObjectType):
    title = graphene.String()
    employer = graphene.String()
    date_started = graphene.Date()
    date_ended = graphene.Date()
    location = graphene.String()
    description = graphene.String()


class EducationSectionInputType(graphene.InputObjectType):
    degree = graphene.String()
    school = graphene.String()
    date_started = graphene.Date()
    date_ended = graphene.Date()
    location = graphene.String()
    years_attended = graphene.Int()


class UserProfileInputType(graphene.InputObjectType):
    title = graphene.String()
    major = graphene.String()
    current_university = graphene.String()
    about = graphene.String()
    employment = graphene.List(EmploymentSectionInputType)
    education = graphene.List(EducationSectionInputType)


class UserSettingsInputType(graphene.InputObjectType):
    subscription_email = graphene.Boolean()
    subscription_sms = graphene.Boolean()
    targeted_advertising = graphene.Boolean()
    language = graphene.String()


class UserInputType(graphene.InputObjectType):
    keycloak_user_id = graphene.String()
    full_name = graphene.String()
    profile = graphene.Field(UserProfileInputType)
    settings = graphene.Field(UserSettingsInputType)
