# pyfilemetre: Python Codebase Analyzer

**pyfilemetre** is a **Python CLI tool** that counts classes and functions, checks for **docstrings**, and generates **Markdown reports** for Python projects. It is designed to give you a clear, file-by-file summary of your codebase quickly.

---

## Features

* Counts **classes and functions**.
* Checks for **missing docstrings**.
* Generates **Markdown reports** summarizing the project.
* Interactive CLI with **spinner animation**.
* Optional flag to **skip saving the report**.

---

## Installation

You can install pyfilemetre from PyPI:

```bash
pip install pyfilemetre
````

> **Note:** Currently not available for local development\!

-----

## Usage

> Run pyfilemetre on a Python file or directory:

```bash
python -m pyfilemetre <path_to_project>
```

**Example:**

```bash
python -m pyfilemetre "C:\Users\You\Desktop\demo_project"
```

> Saving the `report.md` file:

```bash
<path_to_project\report.md>
```

**Example:**

```bash
C:\Users\You\Desktop\demo_project\report.md
```
**Note:** 

  * Do not put the file path in double quotes ("") when entering as path to save report.md file.
  * Always specify `\report.md` at the end of the path you give.

---
### Execution Flow
---
1.  You'll see a **spinner animation** showing progress.
2.  The terminal will display a summary of classes, functions, and docstrings.
3.  You’ll be prompted to save a Markdown report. Enter `y` to save and provide a path, or `n` to skip.

### Optional Flags

  * `--no-md` = Skip saving the Markdown report.

**Example with flag:**

```bash
python -m pyfilemetre "C:\Users\You\Desktop\demo_project" --no-md
```

-----

## Example Output

**Terminal summary:**

```
## 📈 Project Totals
  Total Files: 5
  Total Functions: 20
  Total Classes: 1
  Total Missing Docstrings: 13

# 🧩 pyfilemetre Report
| File | Functions | Classes | Missing Docs |
|------|------------|----------|---------------|
| setup.py | 0 | 0 | 0 |
| analyzer.py | 6 | 1 | 1 |
| cli.py | 2 | 0 | 2 |
| __init__.py | 0 | 0 | 0 |
| test_analyzer.py | 12 | 0 | 10 |
```

  * **Markdown report:** `report.md` generated with the same details per file.


-----

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

-----

## Notes

  * **Python 3.8+** required.
  * Works on Windows, macOS, and Linux.
  * **Tabulate** library is used for nice terminal output.

----
### Created by **[Aditi Gupta](https://aditi-gupta-portfolio.vercel.app/)**.