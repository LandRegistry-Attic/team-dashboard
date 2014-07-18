import pytest
from team.members import Members

def test_init_from_args():
    team = Members()
    team.parse_tsv(
"""name	group	role	photo	slack	twitter	github	aka
Theodore Ruoff	core	Moral Compass	theodore			theodoreruoff	
Robert Roper	core	Business Analyst					rob
""")

    m = team.members['Theodore Ruoff']
    assert m.name == 'Theodore Ruoff'
    assert m.group == 'core'
    assert m.role == 'Moral Compass'
    assert m.photo == 'theodore'
    assert m.github == 'theodoreruoff'

    m = team.members['Robert Roper']
    assert m.name == 'Robert Roper'
    assert m.group == 'core'
    assert m.role == 'Business Analyst'
    assert m.aka == 'rob'
