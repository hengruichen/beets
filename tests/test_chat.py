import pytest
from unittest.mock import MagicMock, patch

from beetsplug.chat import ChatPlugin


@pytest.fixture
def chat_plugin():
    """Create a ChatPlugin instance for testing."""
    return ChatPlugin()


@pytest.fixture
def mock_beets_session():
    """Mock BeetsSession for testing."""
    session = MagicMock()
    # Set up default values for common attributes
    session.config = MagicMock()
    # Add a default value for config.get('chat', {}) to avoid KeyError
    session.config.get.return_value = {}
    return session


@pytest.fixture
def mock_beets_lib():
    """Mock BeetsLibrary for testing."""
    lib = MagicMock()
    # Set up default values for common attributes
    lib.directory = "/test/music"
    lib.config = MagicMock()
    # Add a default value for config.get('chat', {}) to avoid KeyError
    lib.config.get.return_value = {}
    return lib


@pytest.fixture
def mock_beets_log():
    """Mock BeetsLogger for testing."""
    log = MagicMock()
    return log


@pytest.fixture
def mock_beets_user():
    """Mock BeetsUser for testing."""
    user = MagicMock()
    # Set up default values for common attributes
    user.config = MagicMock()
    # Add a default value for config.get('chat', {}) to avoid KeyError
    user.config.get.return_value = {}
    return user


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """Mock user number input for testing."""
    def mock_number(prompt, default=None):
        return 1
    monkeypatch.setattr("beets.ui.user_input.number", mock_number)
    return mock_number


@pytest.fixture
def mock_beets_user_text(monkeypatch):
    """Mock user text input for testing."""
    def mock_text(prompt, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.text", mock_text)
    return mock_text


@pytest.fixture
def mock_beets_user_yesno(monkeypatch):
    """Mock user yes/no input for testing."""
    def mock_yesno(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.yesno", mock_yesno)
    return mock_yesno


@pytest.fixture
def mock_beets_user_input(monkeypatch):
    """Mock user input for testing."""
    def mock_input(prompt):
        return "test"
    monkeypatch.setattr("builtins.input", mock_input)
    return mock_input


@pytest.fixture
def mock_beets_user_confirm(monkeypatch):
    """Mock user confirmation for testing."""
    def mock_confirm(prompt, default=False):
        return True
    monkeypatch.setattr("beets.ui.user_input.confirm", mock_confirm)
    return mock_confirm


@pytest.fixture
def mock_beets_user_choice(monkeypatch):
    """Mock user choice for testing."""
    def mock_choice(prompt, choices, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.choice", mock_choice)
    return mock_choice


@pytest.fixture
def mock_beets_user_options(monkeypatch):
    """Mock user options for testing."""
    def mock_options(prompt, options, default=None):
        return "test"
    monkeypatch.setattr("beets.ui.user_input.options", mock_options)
    return mock_options


@pytest.fixture
def mock_beets_user_number(monkeypatch):
    """