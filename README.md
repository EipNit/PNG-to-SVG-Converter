# PNG to SVG Converter

This project provides a simple utility to convert PNG images to SVG format using a two-step process. It first converts PNG images to PGM format and then uses the `potrace` command-line tool to convert the PGM images to SVG.

## Prerequisites

Before using this tool, ensure you have the following installed:

- Python 3.x
- Pillow library
- Potrace command-line tool

You can install the Pillow library using pip:

```bash
pip install Pillow
