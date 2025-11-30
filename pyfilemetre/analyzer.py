import ast
import os
from tabulate import tabulate

class CodeAnalyzer:
    """
    Analyzes Python code across files or directories using the AST module.

    Features:
    - Counts functions and classes
    - Calculates lines per function/class
    - Detects missing docstrings
    - Generates Markdown reports and terminal summaries
    """

    def __init__(self, path):
        self.path = path
        self.files = self._collect_files(path)

    def _collect_files(self, path):
        """Return list of .py files from a single file or directory."""
        if os.path.isfile(path) and path.endswith(".py"):
            return [path]
        elif os.path.isdir(path):
            py_files = []
            for root, _, files in os.walk(path):
                for f in files:
                    if f.endswith(".py"):
                        py_files.append(os.path.join(root, f))
            # ✅ Deduplicate and sort to avoid duplicate file entries
            return list(sorted(set(py_files)))
        else:
            raise ValueError("Path must be a Python file or a directory containing Python files.")

    def _analyze_file(self, file_path):
        """Analyze one Python file and extract stats."""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()
            tree = ast.parse(code)
        except SyntaxError:
            # Handle files that can't be parsed due to syntax errors
            return {
                "file": file_path,
                "function_count": 0,
                "class_count": 0,
                "functions": [],
                "classes": [],
                "missing_function_docs": 0,
                "missing_class_docs": 0,
            }

        functions, classes = [], []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                lines = getattr(node, "end_lineno", node.lineno) - node.lineno + 1
                docstring = bool(ast.get_docstring(node))
                functions.append({
                    "name": node.name,
                    "lines": lines,
                    "has_docstring": docstring,
                })
            elif isinstance(node, ast.ClassDef):
                lines = getattr(node, "end_lineno", node.lineno) - node.lineno + 1
                docstring = bool(ast.get_docstring(node))
                classes.append({
                    "name": node.name,
                    "lines": lines,
                    "has_docstring": docstring,
                })

        return {
            "file": file_path,
            "function_count": len(functions),
            "class_count": len(classes),
            "functions": functions,
            "classes": classes,
            "missing_function_docs": sum(not f["has_docstring"] for f in functions),
            "missing_class_docs": sum(not c["has_docstring"] for c in classes),
        }

    def analyze(self):
        """Analyze all files and return a summary."""
        file_summaries = [self._analyze_file(f) for f in self.files]

        total_functions = sum(f["function_count"] for f in file_summaries)
        total_classes = sum(f["class_count"] for f in file_summaries)
        missing_docs = sum(
            f["missing_function_docs"] + f["missing_class_docs"]
            for f in file_summaries
        )

        project_summary = {
            "total_files": len(file_summaries),
            "total_functions": total_functions,
            "total_classes": total_classes,
            "total_missing_docstrings": missing_docs,
        }

        return {"files": file_summaries, "project": project_summary}

    def show_terminal_summary(self, result):
        """Pretty-print the results in a table."""
        print("\n📁 Analyzing:", os.path.abspath(self.path))
        print("\n📊 File Summary:\n")

        table = []
        for f in result["files"]:
            table.append([
                os.path.basename(f["file"]),
                f["function_count"],
                f["class_count"],
                f["missing_function_docs"] + f["missing_class_docs"],
            ])

        print(tabulate(table, headers=["File", "Functions", "Classes", "Missing Docs"], tablefmt="github"))
        print("\n📈 Project Totals:")
        for key, value in result["project"].items():
            print(f"  {key.replace('_', ' ').title()}: {value}")

    def save_markdown_report(self, result, output_path="pyfilemetre_report.md"):
        """Save the analysis report in Markdown format."""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# 🧩 pyfilemetre Report\n\n")
            f.write("| File | Functions | Classes | Missing Docs |\n")
            f.write("|------|------------|----------|---------------|\n")
            for fsum in result["files"]:
                f.write(
                    f"| {os.path.basename(fsum['file'])} | "
                    f"{fsum['function_count']} | "
                    f"{fsum['class_count']} | "
                    f"{fsum['missing_function_docs'] + fsum['missing_class_docs']} |\n"
                )

            f.write("\n## 📈 Project Totals\n")
            for key, value in result["project"].items():
                f.write(f"- **{key.replace('_',' ').title()}**: {value}\n")
        print(f"\n📝 Markdown report saved to {output_path}")