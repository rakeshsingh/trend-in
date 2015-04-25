import os
import portal
import unittest
import tempfile

class PortalTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, portal.app.config['DATABASE'] = tempfile.mkstemp()
        portal.app.config['TESTING'] = True
        self.app = portal.app.test_client()
        portal.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(portal.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
