# sets up the config file to enable passwordless login

# set configuration file to use /.ssh/school
file_line { 'Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	Identityfile = ~/.ssh/school',
}

# diable password login
file_line { 'disable password login':
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no',
}
