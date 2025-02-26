import unittest
from unittest.mock import patch
import scripts.interface as interface


class TestGameGUI(unittest.TestCase):

    def setUp(self):
        print("\n------------------------------")

    def test_start_button_calls_on_start_click(self):
        """Verify that clicking the Start button calls on_start_click()."""
        print(" Testing: Start button should call on_start_click()")
        with patch("scripts.interface.on_start_click") as mock_start:
            interface.on_start_click()  # Simulate button press
            mock_start.assert_called_once()
        print(" PASSED: on_start_click() was called correctly.")

    def test_profile_button_calls_on_user_profile_click(self):
        """Verify that clicking the Profile button calls on_user_profile_click()."""
        print(" Testing: Profile button should call on_user_profile_click()")
        with patch("scripts.interface.on_user_profile_click") as mock_profile:
            interface.on_user_profile_click()
            mock_profile.assert_called_once()
        print(" PASSED: on_user_profile_click() was called correctly.")

    def test_statistics_button_calls_on_statistics_click(self):
        """Verify that clicking the Statistics button calls on_statistics_click()."""
        print(" Testing: Statistics button should call on_statistics_click()")
        with patch("scripts.interface.on_statistics_click") as mock_stats:
            interface.on_statistics_click()
            mock_stats.assert_called_once()
        print(" PASSED: on_statistics_click() was called correctly.")

    def test_login_button_calls_on_login_click(self):
        """Verify that clicking the Login button calls on_login_click()."""
        print(" Testing: Login button should call on_login_click()")
        with patch("scripts.interface.on_login_click") as mock_login:
            interface.on_login_click()
            mock_login.assert_called_once()
        print(" PASSED: on_login_click() was called correctly.")

    def test_logout_button_calls_on_log_out_click(self):
        """Verify that clicking the Logout button calls on_log_out_click()."""
        print(" Testing: Logout button should call on_log_out_click()")
        with patch("scripts.interface.on_log_out_click") as mock_logout:
            interface.on_log_out_click()
            mock_logout.assert_called_once()
        print(" PASSED: on_log_out_click() was called correctly.")

    def test_admin_control_button_calls_on_admin_control_click(self):
        """Verify that clicking the Admin Control button calls on_admin_control_click()."""
        print(" Testing: Admin Control button should call on_admin_control_click()")
        with patch("scripts.interface.on_admin_control_click") as mock_admin:
            interface.on_admin_control_click()
            mock_admin.assert_called_once()
        print(" PASSED: on_admin_control_click() was called correctly.")

    def tearDown(self):
        print("------------------------------\n")


if __name__ == "__main__":
    unittest.main()
