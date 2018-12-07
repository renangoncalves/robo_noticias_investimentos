#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
source ./robo_noticias_investimentos/bin/activate

python run.py
