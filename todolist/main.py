from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from todolist import router, seed_data
from todolist.graphql import schema

app = FastAPI(title="ToDo List API")

seed_data()

app.include_router(router)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
