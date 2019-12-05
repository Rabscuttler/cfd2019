test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> spicy_nacho == 'Spicy!'
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> nacho_reaction('cheese')
          'Cheesy!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> nacho_reaction('both')
          'Wow!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> nacho_reaction('neither')
          'Meh.'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
