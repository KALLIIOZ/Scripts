#!/bin/bash

# Verificar si se proporcionaron los parámetros necesarios
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <SSID> <Contraseña>"
    exit 1
fi

# Obtener SSID y contraseña de los argumentos
SSID="$1"
PASSWORD="$2"

# Crear el archivo de configuración para NetworkManager
CONF_FILE="/etc/NetworkManager/system-connections/$SSID.nmconnection"

# Crear el archivo de configuración si no existe
echo "[connection]" > "$CONF_FILE"
echo "id=$SSID" >> "$CONF_FILE"
echo "type=wifi" >> "$CONF_FILE"

echo "[wifi]" >> "$CONF_FILE"
echo "ssid=$SSID" >> "$CONF_FILE"
echo "mode=infrastructure" >> "$CONF_FILE"
echo "password=$PASSWORD" >> "$CONF_FILE"

echo "[ipv4]" >> "$CONF_FILE"
echo "method=auto" >> "$CONF_FILE"

echo "[ipv6]" >> "$CONF_FILE"
echo "method=auto" >> "$CONF_FILE"

# Cambiar permisos del archivo de configuración para que solo el usuario pueda leerlo
chmod 600 "$CONF_FILE"

# Reiniciar NetworkManager para aplicar la configuración
sudo systemctl restart NetworkManager

echo "Conexión configurada para $SSID"