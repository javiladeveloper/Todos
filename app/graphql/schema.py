import strawberry
from strawberry.fastapi import GraphQLRouter

from app.graphql.resolvers import Mutation, Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, path="/graphql")
