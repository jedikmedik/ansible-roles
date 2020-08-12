elk
=======

## Description
Эта роль устанавливает и конфигурирует ELK стек. На данный
момент есть поддержка только Elasticsearch, Kibana, Curator.

По умолчанию ставится лишь Elasticsearch, остальное нужно включать
явно. Если компнонент не ставится, то он и не настраивается. Если
ставится, то настраивается и запускается при загрузке.

По умолчанию все компоненты работают с лупбэком. Curator
автоматически настраивается на обращение к тому адресу, на котором
слушает ES. ВНИМАНИЕ: по умолчанию куратор удаляет все индексы старше
elk_curator_config_keep_indices дней, МОЖНО ПОТЕРЯТЬ ДАННЫЕ! Если
хотите разного срока хранения для разных индексов, нужно задавать
action_file.yml curator-а целиком (elk_curator_action_file)

Обратите ВНИМАНИЕ: булевы переменные в конфигурации ES
(elk_es_options) нужно указывать в нижнем регистре и заключать в
двойные кавычки чтобы сохранить регистр и избежать ошибки "Failed to
parse value [True] cannot be parsed to boolean
[ true/1/on/yes OR false/0/off/no ]" в логе ES. Либо использовать
варианты отличные от true/false.

Также роль настраивает локальное резервное копирование ES.

Текущий шаблон мониторинга Zabbix не умеет работать с ES, не слушающим
на localhost, поэтому рекомендуется для подключений по сети задавать
не внешний IP а network.host: 0.0.0.0 И прикрывать доступ пакетным
фильтром.

Xpack интегрирован в ELK в версии 6 так что опции ссылающиеся на него
(например, в elk_es_options) при использовании ветки 5 и ниже нужно
будет отключить, иначе ES не стартует с ошибкой.

ВНИМАНИЕ: при изменении настроек ПЕРЕЗАПУСКАЕТСЯ: elasticsearch, kibana

## Variables
```yaml
elk_version: int # default: 6: ветка репозитория elasti.co, откуда ставится ES/Kibana

elk_install_es: bool # default: true: нужно ли ставить elasticsearch

elk_es_options: dict # словарь опции для elasticsearch.yml в формате "kind: value", значение по умолчанию:
  network.host: 127.0.0.1
  http.port: 9200
  xpack.security.enabled: "false"
  xpack.monitoring.enabled: "false"

elk_es_jvm_options: dict # default: undefined: словарь опции для jvm.options в формате "kind: value", например:
  Xms: 4g
  Xmx: 4g
# будет преобразовано в аргументы java-машины "-Xms4g -Xmx4g"

elk_install_kibana: bool # default: false: нужно ли ставить kibana
elk_kibana_options: dict # словарь опции для kibana.yml в формате "kind: value", значение по умолчанию:
  server.port: 5601
  server.host: 127.0.0.1
  elasticsearch.url: http://127.0.0.1:9200

elk_install_curator: bool # default: false: нужно ли ставить curator
elk_curator_schedule: string # default: "*/5 * * * * nobody": cron-расписание запуска curator И пользователь, от которого это делается
elk_curator_cronline: string # default: "LC_ALL=en_US.utf-8 /usr/bin/curator --config /etc/curator/config.yml /etc/curator/action_file.yml": строка запуска curator из крона
elk_curator_config_hosts: string # default: 127.0.0.1: IP/DNS-имя хоста с ES для куратора
elk_curator_config_port: int # default: 9200: номер порта ES для куратора
elk_curator_config_keep_indices: int # default: 30: сколько дней хранить индексы
elk_curator_action_file: BLOB # default: undefined: полный action_file.yml для куратора, если определён
```
