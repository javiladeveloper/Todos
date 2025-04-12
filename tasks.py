from invoke import task


@task
def run(c):
    c.run("uvicorn app.main:app --reload")


@task
def test(c):
    c.run("pytest")


@task
def cov(c):
    c.run("coverage run -m pytest && coverage report -m")


@task
def lint(c):
    c.run("flake8 app/ tests/")


@task
def format(c):
    c.run("black app/ tests/")


@task
def check(c):
    c.run("black --check app/ tests/")
    c.run("flake8 app/ tests/")
