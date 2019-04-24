# nginx-log-metrics

nginx-log-metrics


The program collects metrics from nginx logs of a custom format and every 10 seconds resets them to the specified address - either in graphite by udp or in prometheus, depending on the start options.

Programming language: python 3.6

Coding style: the code passed the test flake8

Writing to graphite\prometheus comes from a separate thread.

Logs come to the script via stdin using the command: tail -F /var/log/nginx/access.log | python3 ~nginx-log-metrics.py your_adress -p Flag -p is set to send metrics to prometheus(your_adress=port), in the absence of the flag logs come in graphite(your_adress=graphite_ip port is not specified, it is automatically set to :2003).

Format logs.

log_format main '"$remote_addr" $host $remote_user [$time_local] "$request" '$status $body_bytes_sent "$http_referer" ' "$http_user_agent" $request_id $upstream_addr $upstream_response_time'

Metrics

total_requests - each line of the log increases this counter by 1

upstream_requests - subject to the availability of upstream log uvelchivaetsya 1 total_bytes - increases by $body_bytes_sent

Metrics are stored in the form of:

nginx.<server name.><project name.><metric name> <server name> = socket.gethostname() <project name> is passed as the first parameter of the script.


Программа собирает метрики из логов nginx кастомного формата и каждые 10 секунд сбрасывает их на заданный адрес - либо в graphite по udp, либо в prometheus, в зависимости от опций пуска.

Язык программирования: python3

Стиль кодирования: код прошел проверку flake8

Запись в graphite\prometheus идет из отдельного потока.

Логи поступают скрипту через stdin с помощью команды: tail -F /var/log/nginx/access.log | python3 ~nginx-log-metrics.py your_adress -p Флаг -p выставляется для отправки метрик в prometheus(your_adress=port), в отсутствии флага логи поступают в graphite(your_adress=graphite_ip порт не указывается, он автоматически выставлен :2003).

Формат логов.

log_format main '"$remote_addr" $host $remote_user [$time_local] "$request" ' '$status $body_bytes_sent "$http_referer" ' '"$http_user_agent" $request_id $upstream_addr $upstream_response_time'

Метрики

total_requests - каждая строчка лога увеличивает этот счетчик на 1

upstream_requests - при условии наличия upstream в логе увелчивается на 1
total_bytes - увеличивается на $body_bytes_sent

Метрики сохраняются в виде:

nginx.<имя сервера>.<имя проекта>.<имя метрики> <имя сервера> = socket.gethostname() <имя проекта> передается первым параметром скрипта.


