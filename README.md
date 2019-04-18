# nginx-log-metrics

nginx-log-metrics

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
