from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range()
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_is_less_than_middle_page(self):
        