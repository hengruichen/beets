# Beets Plugin Template

This is a template for creating a new Beets plugin. It includes a basic
structure and documentation to help you get started quickly.

## Getting Started

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Your Plugin:**
   - Edit `beetsplug/template.py` to customize your plugin's functionality
   - Update `README.md` with details about your plugin
   - Add any additional documentation in `docs/`

3. **Test Your Plugin:**
   ```bash
   pytest
   ```

4. **Build Documentation:**
   ```bash
   mkdocs build
   ```

## Plugin Structure

### Core Files

- `beetsplug/template.py` - Main plugin implementation
- `setup.py` - Package configuration
- `README.md` - Plugin documentation
- `docs/` - Additional documentation

### Testing

- `tests/` - Test suite for your plugin
- `pytest.ini` - Pytest configuration

### Documentation

- `mkdocs.yml` - Documentation configuration
- `docs/` - Documentation files

## Development Guidelines

1. **Follow Beets Plugin Standards:**
   - Use the Beets plugin template as a base
   - Follow Beets coding conventions
   - Include comprehensive documentation

2. **Testing:**
   - Write unit tests for all functionality
   - Test edge cases and error conditions
   - Use pytest for testing

3. **Documentation:**
   - Document all public APIs
   - Include usage examples
   - Update documentation when making changes

4. **Versioning:**
   - Use semantic versioning
   - Update version in `setup.py`
   - Update documentation with version changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Update documentation
6. Submit a pull request

## License

This template is licensed under the MIT License. When you create a plugin
based on this template, you should include your own license.

## Support

For support and questions, please:

1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

---

*This template is designed to help you quickly create a new Beets plugin.*
