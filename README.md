# Набор утилит для работы с etherscan

# Установка

1. Иметь установленный `python3` и `pip3`
2. Установить pipenv (https://pipenv.pypa.io/en/latest/) `pip3 install --user pipenv`
3. Определить переменную окружения `export PIPENV_VENV_IN_PROJECT="enabled"` - так pipenv создаст venv в локальном каталоге, это удобнее. Проще всего для этого использовать direnv (https://direnv.net/), чтобы при переходе в каталог переменные настраивались автоматически
4. Выполнить `pipenv install` - создаст окружение и установит зависимости
5. `pipenv shell` - перейдет в настроенное окружение, где уже можно запустить скрипт

## Обновление

Для обновления зависимостей в venv выполнить `pipenv sync`

## fetch_contract_used_gas.py

Собирает с etherscan N последних блоков (10 по-умолчанию, упралвяется через `-b`), сканирует, агрегирует и выдает аналитику по количеству газа использованного для указанных контрактных адресов.

## Пример:

Запуск:

```
> ETHERSCAN_KEY=ТВОЙ_КЛЮЧ ./fetch_contract_used_gas.py \
  0x4dfd148b532e934a2a26ea65689cf6268753e130 \
  0x1f9840a85d5af5bf1d1762f925bdaddc4201f984
```

Выводит:

```
token contract_address	min	med	max
MDT 0x4dfd148b532e934a2a26ea65689cf6268753e130	31351	51729	54135
UNI 0x1f9840a85d5af5bf1d1762f925bdaddc4201f984	25506	90003	172574
```

## Подробнее

```
./fetch_contract_used_gas.py -h
```
