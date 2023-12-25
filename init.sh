if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo."
    exit 1
fi
sudo apt update
sudo apt install build-essential cmake
sudo apt install libopenblas-dev liblapack-dev -y
sudo apt install libx11-dev libgtk-3-dev -y
sudo apt install python3-dev python3-pip -y

export PATH=$PATH:~/.local/bin

python3 -m pip install --upgrade pip

echo 'export OPENBLAS_CORETYPE=ARMV8' >> ~/.bashrc

UDEV_RULES_FILE="/etc/udev/rules.d/99-custom-gpio.rules"
RULES_CONTENT='KERNEL=="gpiochip0", MODE="0666"'

echo "$RULES_CONTENT" | sudo tee "$UDEV_RULES_FILE" > /dev/null
sudo udevadm control --reload-rules