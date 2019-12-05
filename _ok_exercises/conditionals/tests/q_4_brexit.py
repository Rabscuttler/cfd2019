
test = {
  'name': 'Question 4_',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> choose_paper('Soft Brexit')
          'Times'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> choose_paper('Hard Brexit')
          'Telegraph'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> choose_paper('Hard Brexit')
          'Telegraph'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> choose_paper('No-deal Brexit')
          'Daily Express'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> choose_paper('Remain')
          'Guardian'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> choose_paper('remain') is None
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
