# Frequently Asked Questions

This document answers common questions about the Template plugin.

## General Questions

### What is the Template plugin?

The Template plugin is a plugin for the Beets music library manager that provides a set of tools for working with Beets libraries.

### What version of Beets is required?

The Template plugin requires Beets version 1.4.0 or higher.

### How do I install the Template plugin?

To install the Template plugin, add it to your `plugins.yaml` file:

```yaml
plugins:
  - template
```

Then, reload your Beets configuration:

```bash
beet config --reload
```

### How do I update the Template plugin?

To update the Template plugin, reinstall it:

```bash
pip install --upgrade beets-plugin-template
```

### How do I uninstall the Template plugin?

To uninstall the Template plugin, remove it from your `plugins.yaml` file:

```yaml
plugins:
  # Remove the following line
  # - template
```

Then, reload your Beets configuration:

```bash
beet config --reload
```

### Where can I get help with the Template plugin?

You can get help with the Template plugin in the following ways:

1. Check the documentation
2. Search the Beets forums
3. Ask a question on the Beets mailing list
4. Create an issue on the Beets GitHub repository

## Configuration Questions

### How do I configure the Template plugin?

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

### How do I configure the Template plugin for a specific library?

To configure the Template plugin for a specific library, add the following to your `library.yaml` file:

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

### How do I configure the Template plugin for multiple libraries?

To configure the Template plugin for multiple libraries, add the following to your `plugins.yaml` file:

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

## Usage Questions

### How do I use the Template plugin?

To use the Template plugin, add the following to your `plugins.yaml` file:

```yaml
plugins:
  - template
```

Then, reload your Beets configuration:

```bash
beet config --reload
```

### How do I use the Template plugin with a specific library?

To use the Template plugin with a specific library, add the following to your `plugins.yaml` file:

```yaml
plugins:
  - template
```

Then, reload your Beets configuration:

```bash
beet config --reload
```

### How do I use the Template plugin with multiple libraries?

To use the Template plugin with multiple libraries, add the following to your `plugins.yaml` file:

```yaml
plugins:
  - template
```

Then, reload your Beets configuration:

```bash
beet config --reload
```

## Technical Questions

### What programming language is the Template plugin written in?

The Template plugin is written in Python.

### What libraries does the Template plugin use?

The Template plugin uses the following libraries:

- `beets` - The Beets music library manager
- `python-dateutil` - Date and time manipulation
- `python-whoosh` - Full-text search

### What dependencies does the Template plugin have?

The Template plugin has the following dependencies:

- `beets` (>=1.4.0)
- `python-dateutil` (>=2.8.0)
- `python-whoosh` (>=2.7.4)

### What is the Template plugin's license?

The Template plugin is licensed under the MIT License.

## Performance Questions

### How does the Template plugin affect performance?

The Template plugin should have minimal impact on performance. However, if you notice performance issues, you can try the following:

1. Disable the plugin
2. Check your system resources
3. Update your Beets installation
4. Update your Python installation
