# 

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="docs/img/bitcoin-btc-logo.png" alt="Logo" width="80" height="80">
    <img src="docs/img/monero-xmr-logo.png" alt="Logo" width="80" height="80">

  <h3 align="center">Real-time cryptocurrency exchange trade data aggregation system </h3>

  <p align="center">
    This project makes use of the public API <a href="https://docs.poloniex.com/">Poloniex</a>.
    <br />
    <br />
    <a href="https://github.com/gabrielspires/Desafio-Tecnico/tree/main/docs"><strong>Explore the documentation »</strong></a>
    <a href="https://github.com/gabrielspires/Desafio-Tecnico/tree/main/docs/Documentation_pt-br.md">
    <img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/br.png" alt="PT-BR">
    </a>
    <a href="https://github.com/gabrielspires/Desafio-Tecnico/tree/main/docs/Documentation_en-us.md">
    <img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/us.png" alt="EN-US">
    </a>
    <br />
    <br />
    <a href="https://github.com/gabrielspires/Desafio-Tecnico/issues">Report Bug</a>
    ·
    <a href="https://github.com/gabrielspires/Desafio-Tecnico/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project aims at fetching exchange trade data from two popular cryptocurrencies, Monero and Bitcoin, and aggregating it in candlesticks with the information for open, high, low and close for the periods of 1, 5 and 15 minutes. The data used is fetched in realtime from the [Poloniex API](https://docs.poloniex.com/?shell#http-api) and inserted in a local MySQL database after it is aggregated by period of time. The processed data can then be accessed by other applications to create charts and visualizations like the one below for example.

<p align="center">
    <img src="docs/img/candle_chart.png" alt="Candlestick chart" width="100%">
</p>

### Built With

* [Python 3.8.5](https://www.python.org)
* [Docker](https://www.docker.com/)
* [Poetry](https://python-poetry.org/)
* [MariaDB](https://mariadb.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running you'll need the folowing.

### Prerequisites

* [Docker](https://docs.docker.com/engine/install/)
  
* [Docker-compose](https://docs.docker.com/compose/install/)

### Installation

1. Navigate to the project directory and run
   ```sh
   docker-compose up
   ```
    or if you want to repress the container output add the `-d` option
   ```sh
   docker-compose up -d
   ```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Gabriel Pires - [Linkedin](https://www.linkedin.com/in/gabrielhspires/) - gabrielhpires@gmail.com
