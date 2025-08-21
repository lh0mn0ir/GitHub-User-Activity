import pytest

@pytest.fixture
def sample_user_data():
    return {
        "login": "lh0mn0ir",
        "id": 1,
        "avatar_url": "https://github.com/images/error/lh0mn0ir_happy.gif",
        "events_url": "https://api.github.com/users/lh0mn0ir/events{/privacy}",
    }

def test_get_user(sample_user_data):
    from github_cli.controllers import get_user
    username = sample_user_data['login']
    
    user_data = get_user(username)
    
    assert user_data is not None
    assert user_data['login'] == sample_user_data['login']
    assert user_data['id'] == sample_user_data['id']
    assert user_data['avatar_url'] == sample_user_data['avatar_url']
    assert 'events_url' in user_data