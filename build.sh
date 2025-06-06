#!/bin/bash

# Script to build Sphinx documentation with proper PlantUML support
# Usage: ./build.sh [html|pdf|both]

set -e

# Check if PlantUML jar exists
if [ ! -f "plantuml.jar" ]; then
    echo "Downloading PlantUML..."
    curl -L -o plantuml.jar https://github.com/plantuml/plantuml/releases/download/v1.2023.11/plantuml-1.2023.11.jar
fi

# Determine build type
BUILD_TYPE=${1:-both}

# Build HTML
if [ "$BUILD_TYPE" = "html" ] || [ "$BUILD_TYPE" = "both" ]; then
    echo "Building HTML documentation..."
    make html
    echo "HTML documentation built in build/html"
fi

# Build PDF
if [ "$BUILD_TYPE" = "pdf" ] || [ "$BUILD_TYPE" = "both" ]; then
    echo "Building PDF documentation..."
    make latexpdf
    echo "PDF documentation built in build/latex"
    
    # Check if PDF was created
    if [ -f "build/latex/architecturedocumentation.pdf" ]; then
        echo "PDF successfully created:"
        echo "$(pwd)/build/latex/architecturedocumentation.pdf"
    else
        echo "PDF generation may have failed. Check the build/latex directory."
    fi
fi

echo "Documentation build process completed."