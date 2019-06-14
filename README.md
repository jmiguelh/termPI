# termPI

Aplicação para ler a temperatura através da Raspberrypi com o sensor de temperatura DS18B20.

## DS18B20 — Temperature Sensor

Modelo: [Amazon](https://www.amazon.com/dp/B008HODWBU/ref=cm_sw_r_cp_ep_dp_xpI4Ab396BX32)

![Esquema](https://cdn-images-1.medium.com/max/800/0*YyNyjCuxpRrYeif8)

Instação do sensor DS18B20:

* Vcc ==> 3.3V
* Gnd ==> Gnd
* Data ==> GPIO 4 (default for library)

## Google Firebase

 `pip install --upgrade firebase-admin` 

Acesse IAM e administrador > Contas de serviço no Console do Cloud Platform. Gere uma nova chave privada e salve o arquivo JSON. Em seguida, use o arquivo para inicializar o SDK