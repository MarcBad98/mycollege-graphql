import graphene


class EmploymentSectionInputType(graphene.InputObjectType):
    id = graphene.UUID(required=True)
    title = graphene.String()
    employer = graphene.String()
    date_started = graphene.Date()
    date_ended = graphene.Date()
    location = graphene.String()
    description = graphene.String()


class EducationSectionInputType(graphene.InputObjectType):
    id = graphene.UUID(required=True)
    degree = graphene.String()
    school = graphene.String()
    date_started = graphene.Date()
    date_ended = graphene.Date()
    location = graphene.String()


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
    keycloak_user_id = graphene.String(required=True)
    full_name = graphene.String()
    profile = graphene.Field(UserProfileInputType)
    settings = graphene.Field(UserSettingsInputType)
    is_premium = graphene.Boolean()


class FriendsRequestInputType(graphene.InputObjectType):
    pairing = graphene.List(graphene.String, required=True)
    status = graphene.String()
    seen = graphene.Boolean()


class JobApplicationInputType(graphene.InputObjectType):
    applicant = graphene.String()
    date_graduated = graphene.Date()
    date_start = graphene.Date()
    reason = graphene.String()


class JobInputType(graphene.InputObjectType):
    id = graphene.String()
    poster = graphene.String()
    title = graphene.String()
    employer = graphene.String()
    location = graphene.String()
    salary = graphene.String()
    description = graphene.String()
    saved_by = graphene.List(graphene.String)
    applications = graphene.List(JobApplicationInputType)


class MessageInputType(graphene.InputObjectType):
    id = graphene.String()
    sender = graphene.String()
    recipient = graphene.String()
    category = graphene.String()
    message = graphene.String()
    sent_on = graphene.Date()
    seen = graphene.Boolean()
