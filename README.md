# smart-garden

My Smart Garden

## Plan

![garden-plan](plan/garden-plan.png)

## Parts

* ESP8266 NodeMCU
* Sensors
  * BMP280 Temperature Sensor
  * BH1750 Light Sensor

## Run

Run main script directly on the controller:

```shell
ampy --port /dev/tty.<usb-serial-device> run main.py
```

Update main script on the controller

```shell
ampy --port /dev/tty.<usb-serial-device> put main.py
```

