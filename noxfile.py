import nox

@nox.session(python=["3.10.1", "3.9.9"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)

