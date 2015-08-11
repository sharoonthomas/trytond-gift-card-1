# -*- coding: utf-8 -*-
import unittest

import trytond.tests.test_tryton

from tests.test_views_depends import TestViewsDepends
from tests.test_gift_card import TestGiftCard


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestViewsDepends),
        unittest.TestLoader().loadTestsFromTestCase(TestGiftCard),
    ])
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
