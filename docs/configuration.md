# Configuration

This document describes the configuration options for the Template plugin.

## Overview

The Template plugin provides several configuration options to customize its behavior.

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

## Configuration Files

The plugin supports multiple configuration files:

1. **System-wide configuration:**
   ```bash
   ~/.config/beets/plugins.yaml
   ```

2. **User-specific configuration:**
   ```bash
   ~/.config/beets/plugins.yaml
   ```

3. **Library-specific configuration:**
   ```bash
   ~/.config/beets/library.yaml
   ```

## Default Configuration

The plugin uses the following default configuration:

```yaml
# Default configuration for the Template plugin

# Plugin-specific options
template:
  option1: default_value1
  option2: default_value2
```

## Configuration Examples

### Basic Configuration

```yaml
# Basic configuration for the Template plugin

# Plugin-specific options
template:
  option1: value1
  option2: value2
```

### Advanced Configuration

```yaml
# Advanced configuration for the Template plugin

# Plugin-specific options
template:
  option1: value1
  option2: value2
  option3: value3
  option4: value4
```

## Configuration Validation

The plugin validates configuration options:

- Validates that required options are present
- Validates that option values are of the correct type
- Validates that option values are within acceptable ranges

## Configuration Persistence

Configuration changes are persisted across plugin reloads:

1. Configuration changes are saved to the configuration file
2. Configuration is reloaded when the plugin is reloaded
3. Configuration changes are applied immediately

## Configuration Troubleshooting

If you encounter issues with configuration:

1. Check that the configuration file is in the correct location
2. Verify that the configuration file has the correct permissions
3. Check that the configuration file is in the correct format
4. Verify that the configuration file is readable by the user
