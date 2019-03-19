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

```bash
   docker build . --tag=barreios-service
```

- #### Get a cep by address
```http
GET /address/RJ/Santa/29650000 HTTP/1.1
Host: localhost
```
- #### Get an address by cep

```http
GET /cep/01001000 HTTP/1.1
Host: localhost
Content-Type: application/json

```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
