"""
pyfilemetre
--------

A simple Python code analysis tool using the AST module.
Counts functions, classes, and docstrings — and produces summaries and Markdown reports.
"""

from .analyzer import CodeAnalyzer

__version__ = "0.1.0"
__all__ = ["CodeAnalyzer"]