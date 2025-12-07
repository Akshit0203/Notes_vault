Sudo su
Apt get update
apt-get install nginx -y
echo "this is \$(hostname)" \>\> /var/www/html/index.html

Df -h
Lsblk
File -s /dev/xvdf - shows :data tells nothing is there
Mkfs.ext4 /dev/xvdf - make file system extemnsion 4 type
Mkdir /data
Mount /dev/xvdf /data
Mountpoint /data
Cd /data/
