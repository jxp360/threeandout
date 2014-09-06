#!/bin/bash

echo "Please enter the data directory (typically /data):"
read datadir
echo "You entered: "
echo $datadir

echo "Please enter the git user:" 
read gituser
echo "You entered: "
echo $gituser

export DATADIR=$datadir
export GITUSER=$gituser

wget "http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm"
sudo rpm -ivh epel-release-6-8.noarch.rpm

sudo yum install git
sudo yum install python-pip
pip install virtualenvwrapper
echo -e "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo -e "export PROJECT_HOME=$DATADIR/threeandout" >> ~/.bashrc
echo -e "source /usr/bin/virtualenvwrapper.sh" >> ~/.bashrc

source ~/.bashrc    
mkvirtualenv ENVIRONMENT_NAME
cd $DATADIR
git clone https://$GITUSER@github.com/jxp360/threeandout.git
cd threeandout
git checkout develop

sudo yum install python-devel
sudo yum groupinstall "Development tools"
sudo yum install postgresql-devel
sudo yum install libxslt-devel
workon development
pip install -r $DATADIR/threeandout/threeandout/requirements/dev.txt

