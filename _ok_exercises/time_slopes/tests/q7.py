test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing the slope
          >>> np.isclose(sos_errors(16000), 62709.57)
          True
          >>> np.isclose(sos_errors(15000), 24790.27)
          True
          >>> np.isclose(sos_errors(14000), 18852.35)
          True
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
