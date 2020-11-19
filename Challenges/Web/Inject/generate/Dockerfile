FROM php:7.0-apache
#ENV PORT 5000
ENTRYPOINT []
#CMD sed -i "s/80/$PORT/g" /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf && docker-php-entrypoint apache2-foreground

CMD echo "AllowOverride All" >> /etc/apache2/apache2.conf
COPY index.php /var/www/html/
COPY flag.txt /flag

