import sys, os
PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, PATH)

from portal.portal import app

if __name__ == "__main__":
    app.run()    