rabbitMQ:
-install: 
<!-- UPDATE SYSTEM -->
    apt-get update
<!-- ADD REPO AND IMPORT THE KEY -->
    echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
    wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
<!-- UPDATE THE PACKAGES -->
    apt-get update
<!-- INSTALL RABBITMQ SERVER -->
    apt-get install rabbitmq-server
<!-- START & ENABLE THE RABBITMQ_SERVER -->
    systemctl start rabbitmq-server
    systemctl enable rabbitmq-server
<!-- CHECK THE RABBITMQ SERVER STATUS -->
    systemctl status rabbitmq-server
<!-- CREATE USER IN RABBITMQ SERVER -->
    rabbitmqctl add_user admin password
<!-- PROVIDE THE TAGS TO CREATED USER -->
    rabbitmqctl set_user_tags admin administrator
<!-- PROVIDE THE PERMISSION -->
    rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
<!-- ENABLE THE RABBITMQ WEB MANAGEMENT CONSOLE -->
    rabbitmq-plugins enable rabbitmq_management
<!-- OPEN THE PORT NUMBER IN UFW FIREWALL -->
    ufw allow 15672/tcp

Celery:
-install:
    apt-get update
    apt-get -y install celery

FLask:
-install:
    pip install Flask

<!-- GMAIL -->
Use app password instead of normal password to connect third-party app to gmail