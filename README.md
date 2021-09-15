# Набор утилит для работы с etherscan

# Установка

1. Иметь установленный `python3` и `pip3`
2. `make install`

## fetch_contract_used_gas.py

Собирает с etherscan N последних блоков (10 по-умолчанию, упралвяется через `-b`), сканирует, агрегирует и выдает аналитику по количеству газа использованного для указанных контрактных адресов.

## Пример:

Запуск:

```
> ETHERSCAN_KEY=ТВОЙ_КЛЮЧ ./fetch_contract_used_gas.py \
  0x4dfd148b532e934a2a26ea65689cf6268753e130 \
  0x1f9840a85d5af5bf1d1762f925bdaddc4201f984 \
  0x1f9840a85d5af5bf1d1762f925bdaddc4201f984
```

Выводит:

```
contract_address	min	med	max
0x4dfd148b532e934a2a26ea65689cf6268753e130	31351	51729	54135
0x1f9840a85d5af5bf1d1762f925bdaddc4201f984	25506	90003	172574
0x1f9840a85d5af5bf1d1762f925bdaddc4201f984	25506	90003	172574
```

## Подробнее

```
./fetch_contract_used_gas.py -h
```
