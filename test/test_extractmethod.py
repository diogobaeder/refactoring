from nose.tools import istest
from unittest import TestCase

from refactoring.refactoring.extractmethod import TeamReporter


class TeamReporterTest(TestCase):
    @istest
    def reports_all_members_provided(self):
        reporter = TeamReporter()

        result = reporter.report_members('diogo', 'sidnei', 'salgado')
        self.assertEqual(result, 'Team is: Diogo, Sidnei and Salgado')
