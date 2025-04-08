import strawberry
from todolist.graphql_types import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
