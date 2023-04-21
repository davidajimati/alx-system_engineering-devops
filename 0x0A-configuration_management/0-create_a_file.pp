# shell manisfest to create a file in /etc

file{'/etc/school':
  ensure  =>'file',
  mode    =>'0744',
  owner   =>'www-data',
  group   =>'www-data',
  content =>'I love Puppet',
}
