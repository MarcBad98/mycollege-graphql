from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

from app.graphql import schema


def create_app():
    app = Flask(__name__)
    app.add_url_rule(
        "/",
        view_func=GraphQLView.as_view(
            "graphql",
            schema=schema,
            graphiql=True,
        ),
    )
    CORS(app)
    return app
