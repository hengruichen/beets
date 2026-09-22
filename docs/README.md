# Documentation

This directory contains documentation for your Beets plugin.

## Documentation Structure

- `index.md` - Main documentation page
- `usage.md` - Usage and installation instructions
- `api.md` - API documentation
- `examples.md` - Usage examples
- `configuration.md` - Configuration options
- `faq.md` - Frequently asked questions

## Documentation Guidelines

1. **Write Clear Documentation:**
   - Use clear, concise language
   - Provide examples where helpful
   - Explain complex concepts

2. **Keep Documentation Up-to-Date:**
   - Update documentation with each release
   - Document any breaking changes
   - Remove outdated information

3. **Use Markdown:**
   - Follow standard Markdown formatting
   - Include code blocks for examples
   - Use headings to organize content

4. **Include Screenshots:**
   - For GUI plugins, include screenshots
   - Show before/after examples
   - Highlight key features

## Building Documentation

To build the documentation:

```bash
mkdocs build
```

This will generate HTML files in the `site/` directory.

## Deploying Documentation

To deploy the documentation to GitHub Pages:

```bash
mkdocs gh-deploy
```

## Documentation Tools

- **mkdocs** - Documentation generator
- **mkdocs-material** - Beautiful documentation theme
- **mkdocs-jupyter** - Support for Jupyter notebooks
