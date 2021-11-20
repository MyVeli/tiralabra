from invoke import task

@task
def test(ctx):
    ctx.run("python -m pytest src/tests")

@task
def start(ctx):
    ctx.run("python src/main.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src/tests")
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")
