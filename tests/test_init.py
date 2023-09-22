import pytest
from project import create_app, db
from project.models import Improvement, System

@pytest.fixture()
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope="function")
def init_improvement_database(client):
    db.create_all()
    name = "Learn and Be Curious is the way to go"
    system_id = 1
    user_id = 1
    description = "A great idea"

    improvement = Improvement(
        name=name,
        system_id=system_id,
        user_id=user_id,
        description=description,
    )

    name = "System_Overload_Failure"
    system_health = "Healthy"
    priority = 5
    language = "Perl"
    tech_stack = "MAWS"
    description = "Learning is the way to go, sys_call() memory failure"

    system = System(
        name=name,
        system_health=system_health,
        priority=priority,
        language=language,
        tech_stack=tech_stack,
        description=description,
    )

    db.session.add(system)
    db.session.add(improvement)
    db.session.commit()
    yield

    db.drop_all()