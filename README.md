# barreios

A API for fetch data in correios company.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install barreios.

```bash
pip install -r requirements.txt
```
Note: barreios uses [aiohttp](https://aiohttp.readthedocs.io/en/stable/) and requires Python '>=3.4.2'


## Usage

- #### Start the service via docker command

###### Build the app
```bash
   docker build --tag=barreios-service .
```
###### Run the app

```bash
   sudo docker run -p 80:80 -d barreios-service
```

- #### Get a cep by address
###### Request
```http
GET /address/RJ/Santa/29650000 HTTP/1.1
Host: localhost
```
###### Response 
```json
 [
    {
        "cep": "28770-000",
        "logradouro": "",
        "complemento": "",
        "bairro": "",
        "localidade": "Santa Maria Madalena",
        "uf": "RJ",
        "unidade": "",
        "ibge": "3304607",
        "gia": ""
    }
 ]
```
- #### Get an address by cep
###### Request
```http
GET /cep/01001000 HTTP/1.1
Host: localhost
Content-Type: application/json

```
###### Response
``` json
{
    "cep": "01001-000",
    "logradouro": "Praça da Sé",
    "complemento": "lado ímpar",
    "bairro": "Sé",
    "localidade": "São Paulo",
    "uf": "SP",
    "unidade": "",
    "ibge": "3550308",
    "gia": "1004"
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
