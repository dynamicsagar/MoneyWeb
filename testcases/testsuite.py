import unittest
import xmlrunner


from testcases.register.test_register import RegisterTests
from testcases.login.test_login import LoginTests
# from testcases.logout.test_logout import LogoutTests
from testcases.generate_report import GenerateReport


def create_suite(classes):
    suite = unittest.TestSuite()
    for _class in classes:
        _object = _class()
        for function_name in dir(_object):
            if function_name.lower().startswith("test"):
                suite.addTest(_class(function_name))
    return suite


def run_unit_tests():
    runner = xmlrunner.XMLTestRunner(verbosity=2)
    classes = [
        RegisterTests,
        LoginTests,
        # LogoutTests,
        GenerateReport
    ]
    runner.run(create_suite(classes))


if __name__ == "__main__":
    run_unit_tests()
