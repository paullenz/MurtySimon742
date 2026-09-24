"""Regression checks for the actual bold-label handoff parser failure."""
import unittest
from check_status_sync import VALID_MODES, work_mode

class WorkModeTest(unittest.TestCase):
    def test_supported_handoffs(self):
        for mode in VALID_MODES:
            for template in ('WORK MODE: {}', 'WORK MODE: `{}`.',
                             '**WORK MODE:** {}. Explanation.',
                             '**WORK MODE:** `{}`. Explanation.'):
                with self.subTest(mode=mode, template=template):
                    self.assertEqual(work_mode(template.format(mode)), mode)

    def test_rejects_bad_values(self):
        for text in ('no field', 'WORK MODE: MATH2', 'WORK MODE: MATH_EXTRA',
                     '**WORK MODE:** `UNLISTED`.', '**WORK MODE:** `math`.',
                     'WORK MODE: `MATH', 'WORK MODE: MATH_EXTRA',
                     'WORK MODE: MATH-EXTRA', 'WORK MODE: `MATH`EXTRA',
                     'WORK MODE: MATH WORK MODE: AUDIT'):
            with self.subTest(text=text):
                self.assertNotIn(work_mode(text), VALID_MODES)

if __name__ == '__main__':
    unittest.main()
