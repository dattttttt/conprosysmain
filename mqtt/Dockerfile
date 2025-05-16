# mqtt/Dockerfile

FROM eclipse-mosquitto:2.0.15

COPY config/mosquitto.conf /mosquitto/config/mosquitto.conf

EXPOSE 1883
EXPOSE 9001

CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]
