import os
import time
import argparse
import builtins
from .analyzer import CodeAnalyzer

def show_spinner(task_name="Getting information"):
    print(f"{task_name}", end="", flush=True)
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(" Done!\n")

if getattr(builtins, "_pyfilemetre_running", False):
    raise SystemExit(0)
builtins._pyfilemetre_running = True

def main():
    parser = argparse.ArgumentParser(
        description="pyfilemetre — analyze Python code for functions, classes, and docstrings."
    )
    parser.add_argument("path", help="Path to a Python file or directory")
    parser.add_argument(
        "--no-md", action="store_true", help="Skip saving the Markdown report"
    )
    args = parser.parse_args()

    show_spinner("Analyzing project")

    analyzer = CodeAnalyzer(args.path)
    result = analyzer.analyze()
    analyzer.show_terminal_summary(result)

    if not args.no_md:
        save = input("\nDo you want to save the report as a markdown file? (y/n): ").strip().lower()
        if save == "y":
            report_path = input("Enter full path to save report (e.g., C:\\Users\\You\\Desktop\\report.md): ").strip()
            directory = os.path.dirname(report_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            analyzer.save_markdown_report(result, report_path)
        else:
            print("Report not saved.")