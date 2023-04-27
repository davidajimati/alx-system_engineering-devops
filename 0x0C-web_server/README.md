### 0x0C. Web server
This project is focused on:
 - web server configuration
 - child processes
 - Nginx web server
 - Server blocks (virtual servers) 
 - secure shell file transfer
 -  and everything in between to ensure secure and effective file transfer between host and server networks.
 The bash scripts in this directory are capable of automating major host-server interactions needed to launch web pages and virtual servers. 

 The major factors are:
	1. Is the server configured according to requirements
	2. Does the files contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention).

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file (Bash) would contain:
```
david@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```
