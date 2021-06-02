import unittest
import tempfile
import shutil
from src import persistence


class TestPersistence(unittest.TestCase):

    temp_dir = None

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp() + '/'

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_write_and_get_file_data(self):
        entity_name = 'test_entity'
        data_to_persist = {
            '23': {
                'id': '23',
                'name': "Hi, I'm a test entity",
            }
        }

        persistence.write_file_data(self.temp_dir, entity_name, {entity_name: data_to_persist})
        persisted_data = persistence.get_file_data(self.temp_dir, entity_name)

        self.assertEqual(data_to_persist, persisted_data)


if __name__ == '__main__':
    unittest.main()
