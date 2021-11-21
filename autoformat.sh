#/bin/bash
#
# If you get permission error, you can try
# chmod +rx autoformat.sh

echo 'Running isort'
isort -rc mltraining/*
isort -rc api/*

echo 'Running black'
black mltraining/*.py
black api/*.py

echo 'Finished auto formatting'
