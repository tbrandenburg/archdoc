# Architectural Documentation with Sphinx

This repository contains architectural documentation created with Sphinx, sphinx-needs, and PlantUML integration.

## Project Overview

This project demonstrates how to create professional architectural documentation using:
- **Sphinx**: A powerful documentation generator
- **PlantUML**: For creating architectural diagrams through text
- **Sphinx-Needs**: For requirements management
- **LaTeX/PDF**: For A4 PDF generation

## Requirements

To use this project, you'll need:

- Python 3.6+
- Sphinx and extensions (see requirements.txt)
- Java Runtime Environment (for PlantUML)
- LaTeX (for PDF generation)

## Installation

1. Clone this repository
2. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure Java is installed for PlantUML

## Building the Documentation

### HTML Documentation

```bash
cd sphinx
./build.sh html
```

The documentation will be available in `build/html/index.html`.

### PDF Documentation

```bash
cd sphinx
./build.sh pdf
```

The PDF will be generated in `build/latex/architecturedocumentation.pdf`.

### Building Both Formats

```bash
cd sphinx
./build.sh
```

## Project Structure

- `source/`: Contains the reStructuredText files
  - `index.rst`: Main index file
  - `architecture.rst`: Architecture documentation with PlantUML diagram
- `source/_static/`: Static files (CSS, images, etc.)
- `source/_templates/`: Custom templates
- `build/`: Generated documentation (created when building)
- `conf.py`: Sphinx configuration

## Contributing

Feel free to fork this repository and customize it for your own architecture documentation needs.

## License

[MIT License](LICENSE)