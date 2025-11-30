import sys

def run():
    from pyfilemetre.cli import main
    main()

if __name__ == "__main__":
    if not any("pyfilemetre.cli" in arg for arg in sys.argv):
        run()
