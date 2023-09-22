from project.models import Improvement, User, System
from .test_init import client

def test_new_user():
    email = "test@amazon.com"
    password = "testpassword"
    name = "TestyMcTestFace"
    type = "user"

    user = User(name=name, password=password, email=email, type=type)
    assert user.email == email
    assert user.password == password
    assert user.type == type
    assert user.name == name


def test_new_system():
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

    assert system.name == name
    assert system.system_health == system_health
    assert system.priority == priority
    assert system.language == language
    assert system.tech_stack == tech_stack
    assert system.description == description


def test_new_improvement():
    name = "System_Overload_Failure"
    system_id = 1
    user_id = 1
    description = "Learning is the way to go, sys_call() memory failure"

    improvement = Improvement(
        name=name,
        system_id=system_id,
        user_id=user_id,
        description=description,
    )

    assert improvement.name == name
    assert improvement.system_id == system_id
    assert improvement.user_id == user_id
    assert improvement.description == description

