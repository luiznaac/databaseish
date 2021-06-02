import unittest
from src.transactions_management import TransactionsManagement


class TestTransactionsManagement(unittest.TestCase):

    def test_terminate_transaction_should_remove_from_cache(self):
        management = TransactionsManagement()
        username = 'test_user'

        first_user_transaction = management.start_or_get_transaction(username)
        management.terminate_transaction(first_user_transaction.tid)
        second_user_transaction = management.start_or_get_transaction(username)

        self.assertNotEqual(first_user_transaction.tid, second_user_transaction.tid)

    def test_get_transaction_with_invalid_tid_should_return_transaction_for_root(self):
        management = TransactionsManagement()
        username = 'test_user'
        valid_transaction = management.start_or_get_transaction(username)

        root_transaction = management.get_transaction('invalid_tid')

        self.assertNotEqual(valid_transaction.tid, root_transaction.tid)
        self.assertEqual(management.user_tids['ROOT'], root_transaction.tid)

    def test_get_transaction_with_valid_tid_should_return_correct_transaction(self):
        management = TransactionsManagement()
        username = 'test_user'
        expected_transaction = management.start_or_get_transaction(username)

        actual_transaction = management.get_transaction(expected_transaction.tid)

        self.assertEqual(expected_transaction, actual_transaction)

    def test_start_or_get_transaction_should_return_different_transactions_for_different_users(self):
        management = TransactionsManagement()
        username_1 = 'test_user_1'
        username_2 = 'test_user_2'

        transaction_1 = management.start_or_get_transaction(username_1)
        transaction_2 = management.start_or_get_transaction(username_2)

        self.assertNotEqual(transaction_1.tid, transaction_2.tid)

    def test_start_or_get_transaction_should_return_same_transaction_for_same_user(self):
        management = TransactionsManagement()
        username = 'test_user'

        transaction_1 = management.start_or_get_transaction(username)
        transaction_2 = management.start_or_get_transaction(username)

        self.assertEqual(transaction_1, transaction_2)


if __name__ == '__main__':
    unittest.main()
