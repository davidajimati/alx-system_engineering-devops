# sets up the config file to enable passwordless login
file {'~/.ssh/config'
  ensure  => 'present',
  content => 'User ubuntu\  Hostname 54.82.29.159\  IdentityFile ~/.ssh/school\  PasswordAuthentication no',
}
