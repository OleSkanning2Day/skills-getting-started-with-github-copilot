from copy import deepcopy

import pytest

from src import app as app_module


@pytest.fixture
def isolated_activities():
    original_activities = deepcopy(app_module.activities)

    yield

    app_module.activities.clear()
    app_module.activities.update(original_activities)
