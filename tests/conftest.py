import pytest
from app import create_app


@pytest.fixture(scope='session')
def app(request):
    """Create an application context."""
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app
