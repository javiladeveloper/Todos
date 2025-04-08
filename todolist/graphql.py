import strawberry

from todolist.graphql_types import Mutation, Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
