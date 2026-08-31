import os
import shutil
from pyfilemetre.analyzer import CodeAnalyzer

TEST_DIR = os.path.join(os.path.dirname(__file__), "test_files")

def setup_module(module):
    """Create a temporary directory for testing."""
    os.makedirs(TEST_DIR, exist_ok=True)

def teardown_module(module):
    """Clean up the temporary test directory."""
    shutil.rmtree(TEST_DIR)

def write_file(filename, content):
    path = os.path.join(TEST_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    return path

def test_single_file():
    file_path = write_file("sample1.py", "def foo(): pass\nclass Bar: pass\n")
    analyzer = CodeAnalyzer(file_path)
    result = analyzer.analyze()
    assert result["files"][0]["function_count"] == 1
    assert result["files"][0]["class_count"] == 1
    assert result["files"][0]["missing_function_docs"] == 1
    assert result["files"][0]["missing_class_docs"] == 1

def test_multiple_functions_classes():
    content = """
def a(): pass
def b(): pass
class X: pass
class Y: pass
"""
    file_path = write_file("sample2.py", content)
    analyzer = CodeAnalyzer(file_path)
    result = analyzer.analyze()
    assert result["files"][0]["function_count"] == 2
    assert result["files"][0]["class_count"] == 2
    assert result["files"][0]["missing_function_docs"] == 2
    assert result["files"][0]["missing_class_docs"] == 2

def test_with_docstrings():
    content = '''
def foo():
    """I have a docstring"""
    pass

class Bar:
    """Class docstring"""
    pass
'''
    file_path = write_file("sample3.py", content)
    analyzer = CodeAnalyzer(file_path)
    result = analyzer.analyze()
    assert result["files"][0]["missing_function_docs"] == 0
    assert result["files"][0]["missing_class_docs"] == 0

def test_empty_file():
    file_path = write_file("empty.py", "")
    analyzer = CodeAnalyzer(file_path)
    result = analyzer.analyze()
    assert result["files"][0]["function_count"] == 0
    assert result["files"][0]["class_count"] == 0
    assert result["files"][0]["missing_function_docs"] == 0
    assert result["files"][0]["missing_class_docs"] == 0

def test_directory_analysis():
    # Already created files in TEST_DIR
    analyzer = CodeAnalyzer(TEST_DIR)
    result = analyzer.analyze()
    assert result["project"]["total_files"] >= 4  # some extra test files might exist

def test_nested_functions():
    content = '''
def outer():
    """Outer function"""
    def inner(): pass
    return inner
'''
    file_path = write_file("nested_func.py", content)
    analyzer = CodeAnalyzer(file_path)
    result = analyzer.analyze()
    assert result["files"][0]["function_count"] == 2
    assert result["files"][0]["missing_function_docs"] == 1  

def test_class_with_methods():
    content = '''
class MyClass:
    """Class docstring"""
    def method_one(self): pass
    def method_two(self):
        """Method docstring"""
        pass
'''
    file_path = write_file("class_methods.py", content)
    analyzer = CodeAnalyzer(file_path)
    result = analyzer.analyze()
    assert result["files"][0]["class_count"] == 1
    assert result["files"][0]["function_count"] == 2
    assert result["files"][0]["missing_function_docs"] == 1
    assert result["files"][0]["missing_class_docs"] == 0

def test_async_function():
    content = '''
async def async_func(): pass
'''
    file_path = write_file("async_func.py", content)
    analyzer = CodeAnalyzer(file_path)
    result = analyzer.analyze()
    assert result["files"][0]["function_count"] == 1
    assert result["files"][0]["missing_function_docs"] == 1

def test_nested_classes():
    content = '''
class Outer:
    """Outer class"""
    class Inner:
        pass
'''
    file_path = write_file("nested_class.py", content)
    analyzer = CodeAnalyzer(file_path)
    result = analyzer.analyze()
    assert result["files"][0]["class_count"] == 2
    assert result["files"][0]["missing_class_docs"] == 1