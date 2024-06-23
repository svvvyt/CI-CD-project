#!/bin/bash

# Загрузка переменных окружения из .env файла
source "$(dirname "$0")/.env"

TESTS_FOLDER='/devops-examples/EXAMPLE_APP/tests'

mkdir -p ${TESTS_FOLDER}/test_res;

function flake8_test() {
    echo "STARTED FLAKE8 TEST";

    flake8 . \
    > >(tee -a "${TESTS_FOLDER}/test_res/flake8.log") \
    2>&1;

    echo "FINISHED FLAKE8 TEST";
}

function pylint_test() {
    echo "STARTED PYLINT TEST";

    touch __init__.py;

    pylint $(pwd) -v --rcfile=${TESTS_FOLDER}/pylintrc \
    > >(tee -a "${TESTS_FOLDER}/test_res/pylint.log") \
    2>&1;

    rm __init__.py;

    echo "FINISHED PYLINT TEST";
}

function integration_test() {
    echo "STARTED INTEGRATION TEST";

    pytest -s -v ${TESTS_FOLDER}/integration_test.py \
    > >(tee -a "${TESTS_FOLDER}/test_res/integration.log") \
    2>&1;

    echo "FINISHED INTEGRATION TEST";
}

function selenium_test() {
    echo "STARTED SELENIUM TEST";

    exec -a xvfb-run Xvfb :1 -screen 0 1920x1080x16 &> xvfb.log  &

    DISPLAY=:1.0
    export DISPLAY

    python3 ${TESTS_FOLDER}/selenium_test/main.py \
    > >(tee -a "${TESTS_FOLDER}/test_res/selenium.log") \
    2>&1;

    kill $(pgrep -f xvfb-run)

    echo "FINISHED SELENIUM TEST";
}

if [ $# -eq 0 ]; then
    IFS=' ' read -r -a stages <<< "$TEST_STAGES"
    for stage in "${stages[@]}"; do
        $stage
    done
else
    $1
fi
