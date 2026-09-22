# Template Plugin Documentation

Welcome to the documentation for the Template plugin. This plugin provides a set of tools for working with Beets libraries.

## Overview

The Template plugin is a plugin for the Beets music library manager that provides a set of tools for working with Beets libraries.

## Features

- **Item Management:** Add, edit, and delete items from the library
- **Album Management:** Add, edit, and delete albums from the library
- **Search:** Search for items and albums by various criteria
- **Export:** Export items and albums to various formats
- **Import:** Import items and albums from various sources

## Installation

To install the Template plugin, add it to your `plugins.yaml` file:

```yaml
plugins:
  - template
```

Then, reload your Beets configuration:

```bash
beet config --reload
```

## Configuration

To configure the Template plugin, add the following to your `plugins.yaml` file:

```yaml
# Configuration for the Template plugin

# Plugin-specific options
template:
  option1: value1
  option2: value2
```

Then, reload your Beets configuration:

```bash
beet config --reload
```

## Usage

To use the Template plugin, add the following to your `plugins.yaml` file:

```yaml
plugins:
  - template
```

Then, reload your Beets configuration:

```bash
beet config --reload
```

### Basic Usage

```bash
# Add an item to the library
beet add /path/to/music/file.mp3

# Add multiple items to the library
beet add /path/to/music/file1.mp3 /path/to/music/file2.mp3

# Search for items by title
beet search "song title"

# Search for items by artist
beet search "artist name"

# Search for items by album
beet search "album name"
```

### Advanced Usage

```bash
# Create a custom query
beet search "artist:beets AND genre:rock"

# Create a complex query
beet search "artist:beets OR artist:beets-plugins"

# Sort results by title
beet search "song title" --sort title

# Sort results by artist
beet search "artist name" --sort artist

# Sort results by year
beet search "album year" --sort year
```

## Commands

The Template plugin provides the following commands:

### `template-command1`

Description: A command for performing action 1.

```bash
beet template-command1 [options]
```

Options:

- `--option1`: Description of option 1
- `--option2`: Description of option 2

### `template-command2`

Description: A command for performing action 2.

```bash
beet template-command2 [options]
```

Options:

- `--option1`: Description of option 1
- `--option2`: Description of option 2

## Hooks

The Template plugin provides the following hooks:

### `item_added`

Called when an item is added to the library.

```python
def item_added(self, item):
    """Called when an item is added to the library."""
    # Your implementation here
    pass
```

### `album_added`

Called when an album is added to the library.

```python
def album_added(self, album):
    """Called when an album is added to the library."""
    # Your implementation here
    pass
```

## Events

The Template plugin provides the following events:

### `plugin_loaded`

Called when the plugin is loaded.

```python
def plugin_loaded(self):
    """Called when the plugin is loaded."""
    # Your implementation here
    pass
```

### `plugin_unloaded`

Called when the plugin is unloaded.

```python
def plugin_unloaded(self):
    """Called when the plugin is unloaded."""
    # Your implementation here
    pass
```

## Error Handling

The Template plugin includes comprehensive error handling:

```python
try:
    # Your code here
    pass
except Exception as e:
    self._log.error(f"Error: {e}")
    raise UserError(f"An error occurred: {e}")
```

## Testing

To test the plugin:

```bash
pytest
```

## Examples

For examples of how to use the Template plugin, see the [Examples](examples.md) documentation.

## Configuration

For information about configuring the Template plugin, see the [Configuration](configuration.md) documentation.

## API Documentation

For detailed API documentation, see the [API Documentation](api.md) documentation.

## Contributing

Contributions are welcome! Please see the [Contributing](contributing.md) documentation for more information.

## License

This plugin is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Support

For support and questions, please:

1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

## Changelog

### Version 1.0.0

- Initial release

## Acknowledgments

Thanks to the Beets community for their support and contributions.
