import graphene


class EmploymentSectionInputType(graphene.InputObjectType):
    id = graphene.UUID()
    title = graphene.String()
    employer = graphene.String()
    date_started = graphene.Date()
    date_ended = graphene.Date()
    location = graphene.String()
    description = graphene.String()


class EducationSectionInputType(graphene.InputObjectType):
    id = graphene.UUID()
    degree = graphene.String()
    school = graphene.String()
    date_started = graphene.Date()
    date_ended = graphene.Date()
    location = graphene.String()
    description = graphene.String()


class UserProfileInputType(graphene.InputObjectType):
    full_name = graphene.String()
    university = graphene.String()
    major = graphene.String()
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
    is_plus_user = graphene.Boolean()
    profile = graphene.Field(UserProfileInputType)
    settings = graphene.Field(UserSettingsInputType)
    # query operations
    friends = graphene.String(name="friend")
    # update operations
    push__friends = graphene.String(name="addFriend")
    pull__friends = graphene.String(name="removeFriend")
    push__jobs_saved = graphene.String(name="saveJob")
    pull__jobs_saved = graphene.String(name="unsaveJob")
    push__courses = graphene.String(name="takeCourse")


class MessageInputType(graphene.InputObjectType):
    id = graphene.String()
    sender = graphene.String()
    recipient = graphene.String()
    category = graphene.String()
    title = graphene.String()
    message = graphene.String()
    resolved = graphene.Boolean()


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
    applications = graphene.List(JobApplicationInputType)
    # query operations
    applications__match = graphene.Field(
        JobApplicationInputType,
        name="matchJobApplication",
    )
    # update operations
    push__applications = graphene.Field(
        JobApplicationInputType,
        name="addJobApplication",
    )


class CourseInputType(graphene.InputObjectType):
    id = graphene.String()
    title = graphene.String()
    auth_required = graphene.Boolean()
