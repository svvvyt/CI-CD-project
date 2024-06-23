#
# Сборка и запуск контейнеров

Чтобы собрать образы контейнеров для приложения и тестов, выполнить в директории c docker-compose.yml:

```bash
docker compose build
```

Чтобы создать и запустить контейнеры из собранных образов в detached mode, выполнить:

```bash
docker compose up -d
```
#
# Тесты и их конфигурация

Когда контейнеры поднялись, можно запустить **все тесты подряд** следующей командой:

```bash
docker exec azar-tester bash ./tests/run_all.sh
```

Конфигурация для порядка этапов тестирования, которые будут запущены в таком случае, расположена в `.env` файле в `tests`:

```
TEST_STAGES="flake8_test pylint_test integration_test selenium_test"
```

Для запуска **только теста на соответствие стилю кодирования (flake8)**, выполнить:

```bash
docker exec azar-tester bash ./tests/run_all.sh flake8_test
```

Для запуска **только теста для статического анализа (pylint)**, выполнить:

```bash
docker exec azar-tester bash ./tests/run_all.sh pylint_test
```

Для запуска **только интеграционного теста**, выполнить:

```bash
docker exec azar-tester bash ./tests/run_all.sh integration_test
```

Для запуска **только selenium-теста**, выполнить:

```bash
docker exec azar-tester bash ./tests/run_all.sh selenium_test
```

- `flake8_test`, `pylint_test`, `integration_test` тестируют веб-приложение из https://github.com/moevm/devops-examples.git.
- `selenium_test` нужен для автотестирования ИС ИОТ: https://dev.digital.etu.ru/trajectories-test/. Сценарий - _"Создание ОПОП, проверка выдачи прав и истории изменений"_

В процессе тестирования генерируются .log-файлы с результатами выполнения тестов. При сборке контейнера определяется монтирование файлов, чтобы с ними можно было дальше работать на хосте:

- `./tests/test_res/<name-of-test-stage>.log` - путь к логам для конкретного типа тестирования
#
# Получение доступа к контейнеру `azar-tester` по SSH

При сборке контейнера `azar-tester` устанавливается SSH-клиент openssh.

- Публичный ключ, используемый в контейнере для внешнего доступа по SSH: `./tester/ssh-keys/id-rsa.pub`

Чтобы получить доступ к `azar-tester` по SSH, выполнить:

```bash
ssh root@127.0.0.1 -p 3023 -i <path-to-private-key>
```
