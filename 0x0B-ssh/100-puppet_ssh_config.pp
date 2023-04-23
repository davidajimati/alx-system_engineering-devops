file {'~/.ssh/school'
  ensure  => 'present',
  content => @(EOF)
User ubuntu
  Hostname 54.82.29.159
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
EOF

}
