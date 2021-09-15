# Набор утилит для работы с etherscan

## fetch_contract_used_gas

Агрегирует и выдает аналитику по количеству газа использованного для указанных контрактных адресов.


Консольная тулза, которая принимает из ENV ключ для эзерскана, аргументом принимает количество блоков которые нас интересуют (10 по-умолчанию), списком через пробел принимает контрактные адреса для отслеживания, через -h рассказывает о себе (название, автор, аргументы, ожидаемые переменные окружения, выдает в STDOUT сборную информацию по минимальному количеству газа, медиана, максимальное по каждому контракту, в качестве разделителя - табуляция.

Пример:

```
> ETHERSCAN_KEY=123 fetch_contract_used_gas.py 0x4dfd148b532e934a2a26ea65689cf6268753e130 0x1f9840a85d5af5bf1d1762f925bdaddc4201f984 0x1f9840a85d5af5bf1d1762f925bdaddc4201f984

contract_address min med max
0x4dfd148b532e934a2a26ea65689cf6268753e130 50000 55000 60000
0x1f9840a85d5af5bf1d1762f925bdaddc4201f984 54000 58000 62000
...
```

Аргументы:

`-b 10` - количество сканируемых блоков
`остальные` - список контрактных адресов через пробел
