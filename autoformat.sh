#/bin/bash
#
# If you get permission error, you can try
# chmod +rx autoformat.sh

echo 'Running isort'
isort -rc mltraining/*

echo 'Running black'
black mltraining/*.py

echo 'Finished auto formatting'
