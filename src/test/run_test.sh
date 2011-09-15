#!/bin/sh


for TESTFILE in test_*.py
    do
    echo =========================================
    echo $TESTFILE
    python $TESTFILE
    done

