# API Documentation

This document provides detailed API documentation for the Template plugin.

## Overview

The Template plugin provides a set of tools for working with Beets libraries.

## Core Classes

### TemplatePlugin

The main plugin class that extends `BeetsPlugin`.

```python
class TemplatePlugin(BeetsPlugin):
    """Template plugin for beets."""

    def __init__(self):
        """Initialize the plugin."""
        super().__init__()

        # Configuration
        self.config.add({
            # Add your configuration options here
        })

        # Commands
        self._commands = []

        # Hooks
        self._register_hooks()
```

### TemplateCommand

A command that extends `beets.ui.command.Command`.

```python
class TemplateCommand(Command):
    """A command for the Template plugin."""

    def __init__(self, name, help_text, aliases=None):
        """Initialize the command."""
        super().__init__(name, help_text, aliases=aliases)

        # Command-specific configuration
        self.config.add({
            # Add your command-specific configuration here
        })

        # Register the command
        self._register_command()
```

## Configuration Options

### Plugin Configuration

```yaml
# Configuration for the Template plugin

# Plugin-specific options
template:
  option1: value1
  option2: value2
```

### Command Configuration

```yaml
# Configuration for the Template plugin

# Command-specific options
template:
  command1:
    option1: value1
    option2: value2
  command2:
    option1: value1
    option2: value2
```

## Commands

### template-command1

Description: A command for performing action 1.

```bash
beet template-command1 [options]
```

Options:

- `--option1`: Description of option 1
- `--option2`: Description of option 2

### template-command2

Description: A command for performing action 2.

```bash
beet template-command2 [options]
```

Options:

- `--option1`: Description of option 1
- `--option2`: Description of option 2

## Hooks

### Item Added Hook

Called when an item is added to the library.

```python
def item_added(self, item):
    """Called when an item is added to the library."""
    # Your implementation here
    pass
```

### Album Added Hook

Called when an album is added to the library.

```python
def album_added(self, album):
    """Called when an album is added to the library."""
    # Your implementation here
    pass
```

## Events

### Plugin Events

- `plugin_loaded`: Called when the plugin is loaded
- `plugin_unloaded`: Called when the plugin is unloaded

### Command Events

- `command_started`: Called when a command is started
- `command_finished`: Called when a command is finished

## Error Handling

The plugin includes comprehensive error handling:

```python
try:
    # Your code here
    pass
except Exception as e:
    self._log.error(f"Error: {e}")
    raise UserError(f"An error occurred: {e}")
```

## Testing

To test the API:

```bash
pytest
```

## Examples

### Basic Usage

```python
from beetsplug.template import TemplatePlugin

plugin = TemplatePlugin()
plugin.load_plugins()
```

### Configuration

```yaml
# Configuration for the Template plugin

# Plugin-specific options
template:
  option1: value1
  option2: value2
```

### Command Usage

```bash
# Run a command
beet template-command1 --option1 value1

# Run another command
beet template-command2 --option1 value1
```

## Best Practices

1. **Error Handling:**
   - Always handle exceptions gracefully
   - Provide meaningful error messages
   - Log errors for debugging

2. **Configuration:**
   - Use sensible default values
   - Document all configuration options
   - Validate configuration values

3. **Documentation:**
   - Document all public APIs
   - Include examples
   - Keep documentation up-to-date

4. **Testing:**
   - Write unit tests
   - Test edge cases
   - Test error conditions

## Contributing

When contributing to the API:

1. Follow the existing code style
2. Add comprehensive documentation
3. Include tests for new functionality
4. Update documentation as needed
