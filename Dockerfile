FROM nginx:alpine
LABEL viki-vik v0.0.3

COPY html/index.html /usr/share/nginx/html
COPY html/script.js /usr/share/nginx/html

RUN set -x ; \
  addgroup -g 82 -S www-data ; \
  adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1
  
# Copy existing application directory permissions
#COPY --chown=www-data:www-data . /usr/share/nginx/html

RUN chown -R www-data:www-data /usr/sbin/nginx

# Change current user to www
# USER www-data

EXPOSE 80
# WORKDIR /
ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-g","daemon off;"]
