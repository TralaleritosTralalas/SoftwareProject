export default {
  extends: ['@commitlint/config-conventional'],

  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',     // New functionality
        'fix',      // Fixing some error
        'docs',     // Documentation
        'style',    // Format and design
        'refactor', // Rewriting the code without fixing anything specific
        'perf',     // Improve the performance
        'test',     // Adding tests
        'chore',    // Management tasks
        'revert'    // Revert a commit
      ]
    ],
    'type-case': [2, 'always', 'lower-case'],
    'subject-empty': [2, 'never'],
  }
};