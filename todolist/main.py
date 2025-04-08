from fastapi import FastAPI
from todolist import router, seed_data
from todolist.graphql import schema
from strawberry.fastapi import GraphQLRouter

app = FastAPI(title="ToDo List API")

seed_data()

app.include_router(router)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
