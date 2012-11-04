class TeamReporter(object):
    def report_members(self, *members):
        members = [member.capitalize() for member in members]

        members_joined = ', '.join(members)
        members_joined = members_joined.replace(', %s' % members[-1],
                                                ' and %s' % members[-1])

        final_result = 'Team is: %s' % members_joined
        return final_result