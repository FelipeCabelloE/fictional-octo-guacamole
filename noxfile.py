# noxfile.py
import nox


@nox.session(python=["3.8", "3.9"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)