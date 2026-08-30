# Contributing to YouTube Downloader

Thank you for your interest in contributing to this project! We welcome contributions from developers of all experience levels. This document provides guidelines to ensure a smooth collaboration experience.

## Getting Started

### Prerequisites
- GitHub account
- Git installed locally
- Python 3.8 or higher
- Basic familiarity with Git workflow

### Setup Instructions

1. **Fork the Repository**
   - Click the "Fork" button in the top-right corner of the GitHub repository

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/descriptive-feature-name
   ```
   Branch naming convention: `feature/`, `bugfix/`, `docs/`, `refactor/`

4. **Set Up Development Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Development Guidelines

### Code Standards

- **Python Style**: Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- **Naming**: Use clear, descriptive variable and function names
- **Comments**: Include docstrings and inline comments for complex logic
- **Type Hints**: Use Python type hints where applicable
- **Testing**: Test changes thoroughly before submission

### Commit Best Practices

- Write clear, descriptive commit messages in imperative mood
- Format: `<type>: <subject>` (e.g., `feat: add subtitle download support`)
- Types: `feat`, `fix`, `docs`, `refactor`, `style`, `test`, `chore`
- Keep commits atomic and logically separate
- Reference related issues: `Fixes #123` or `Related to #456`

### Documentation

- Update README.md for user-facing changes
- Update CHANGELOG.md with new features and fixes
- Add docstrings to new functions and classes
- Include inline comments for complex algorithms
- Update this CONTRIBUTING.md if guidelines change

## Submitting Changes

### Before You Submit

- [ ] Code follows PEP 8 standards
- [ ] All changes are tested locally
- [ ] Commit messages are clear and descriptive
- [ ] Documentation is updated if necessary
- [ ] No merge conflicts with main branch

### Pull Request Process

1. **Ensure Your Branch is Updated**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push Your Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request on GitHub**
   - Use a clear, descriptive title
   - Provide a detailed description including:
     - What changes were made
     - Why the changes are necessary
     - How to test the changes
     - Reference related issues (e.g., `Fixes #123`)
   - Link to any related issues or PRs
   - Include before/after screenshots if UI changes

4. **Address Review Feedback**
   - Respond to reviewer comments professionally
   - Make requested changes promptly
   - Re-request review after updates

5. **Merge**
   - Once approved, a maintainer will merge your PR
   - Your contribution will be included in the next release

## Reporting Bugs

Bug reports help us improve! Please provide:

### Essential Information

- **Environment**
  - Operating System and version (e.g., Ubuntu 22.04, macOS 12.5)
  - Python version: `python3 --version`
  - GTK version: `pkg-config --modversion gtk4`
  - Application version

- **Reproduction Steps**
  1. Step-by-step instructions to reproduce
  2. URL or content used (if applicable)
  3. Expected vs actual behavior

- **Error Details**
  - Complete error message or stack trace
  - Application logs (if available)
  - Screenshots or screen recording

### Bug Report Template

```markdown
**Description**: Brief description of the bug

**Steps to Reproduce**:
1. ...
2. ...
3. ...

**Expected Behavior**: What should happen

**Actual Behavior**: What actually happens

**Environment**: OS, Python version, GTK version

**Logs/Error**: Error messages or logs
```

## Feature Requests

We love hearing new ideas! When suggesting features, please include:

### Feature Request Template

```markdown
**Title**: Brief description of feature

**Problem Statement**: What problem does this solve?

**Proposed Solution**: How should the feature work?

**Use Cases**: Specific scenarios where this would be useful

**Implementation Notes**: Any technical considerations or suggestions

**Alternatives**: Other solutions considered
```

### What Makes a Good Feature Request

- Clearly defined use case and benefit
- Alignment with project goals
- Realistic implementation scope
- No duplication of existing requests

## Code of Conduct

All contributors are expected to adhere to the following principles:

- **Respect** - Treat all community members with courtesy and professionalism
- **Inclusivity** - Welcome contributors of all backgrounds and experience levels
- **Constructive Feedback** - Provide helpful, actionable criticism
- **Collaboration** - Work together toward project success
- **Integrity** - Be honest and transparent in all interactions

### Unacceptable Behavior

The following will not be tolerated:
- Harassment or discrimination based on identity
- Abusive language or personal attacks
- Trolling or deliberately disruptive behavior
- Plagiarism or intellectual property violations

Any violations should be reported to project maintainers immediately.

## Getting Help

- **Questions**: Open an issue with the `question` label
- **Discussions**: Use GitHub Discussions for general topics
- **Technical Issues**: Consult the Troubleshooting section in README.md
- **Direct Contact**: Reach out to project maintainers

## Recognition

All contributors are recognized in:
- Git commit history
- GitHub contributor list
- Project CHANGELOG.md

---

**Thank you for making this project better!** 🙌

For additional information, see the [README.md](README.md) and [CHANGELOG.md](CHANGELOG.md).
