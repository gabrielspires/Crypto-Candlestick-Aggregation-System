# 

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="docs/img/bitcoin-btc-logo.png" alt="Logo" width="80" height="80">
    <img src="docs/img/monero-xmr-logo.png" alt="Logo" width="80" height="80">

  <h3 align="center">Sistema de agregação de dados de cotações de criptomoedas em tempo real</h3>

  <p align="center">
    Esse projeto faz uso da API pública <a href="https://docs.poloniex.com/">Poloniex</a>.
    <br />
    <br />
    <a href="https://github.com/gabrielspires/Desafio-Tecnico/tree/main/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <strong>
    <a href="https://github.com/gabrielspires/Desafio-Tecnico/issues">Report Bug</a>
    ·
    <a href="https://github.com/gabrielspires/Desafio-Tecnico/issues">Request Feature</a>
    </strong>
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
    <!-- <li><a href="#usage">Usage</a></li> -->
    <li><a href="#main-difficulties">Main difficulties</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

....

### Built With

* [Python 3.8.5](https://www.python.org)
* [Docker](https://www.docker.com/)
* [Poetry](https://python-poetry.org/)
* [MariaDB](https://mariadb.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running you'll need the folowing.

### Prerequisites

* docker
  ```sh
  sudo apt-get remove docker docker-engine docker.io containerd runc
  sudo apt-get update
  sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io  
  ```
* docker-compose
  ```sh
  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  ```
<!-- * prerequisite
  ```sh
   
  ``` -->

### Installation

1. Navigate to the project directory and run
   ```sh
   docker-compose up
   ```
    or if you want to repress the container output add the `-d` option
   ```sh
   docker-compose up -d
   ```

<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->

## Main difficulties 

...
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
