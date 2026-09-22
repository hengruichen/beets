# Usage Examples

This document provides examples of how to use the Template plugin.

## Basic Usage

### Adding Items

```bash
# Add an item to the library
beet add /path/to/music/file.mp3

# Add multiple items to the library
beet add /path/to/music/file1.mp3 /path/to/music/file2.mp3
```

### Searching Items

```bash
# Search for items by title
beet search "song title"

# Search for items by artist
beet search "artist name"

# Search for items by album
beet search "album name"
```

### Filtering Items

```bash
# Filter items by genre
beet search "genre:rock"

# Filter items by year
beet search "year:2020"

# Filter items by rating
beet search "rating:>3"
```

## Advanced Usage

### Custom Queries

```bash
# Create a custom query
beet search "artist:beets AND genre:rock"

# Create a complex query
beet search "artist:beets OR artist:beets-plugins"
```

### Sorting Results

```bash
# Sort results by title
beet search "song title" --sort title

# Sort results by artist
beet search "artist name" --sort artist

# Sort results by year
beet search "album year" --sort year
```

### Exporting Results

```bash
# Export results to a file
beet search "song title" --export results.txt

# Export results to a CSV file
beet search "song title" --export results.csv
```

## Command Examples

### Template Command 1

```bash
# Run the first template command
beet template-command1

# Run the first template command with options
beet template-command1 --option1 value1 --option2 value2
```

### Template Command 2

```bash
# Run the second template command
beet template-command2

# Run the second template command with options
beet template-command2 --option1 value1 --option2 value2
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

## Best Practices

1. **Use Clear Queries:**
   - Use descriptive queries
   - Use specific terms
   - Use logical operators

2. **Use Sorting:**
   - Sort by relevant fields
   - Use multiple sorting criteria
   - Use descending order for dates

3. **Use Filtering:**
   - Filter by relevant fields
   - Use logical operators
   - Use range filters

4. **Use Exporting:**
   - Export to files
   - Export to CSV files
   - Export to other formats
