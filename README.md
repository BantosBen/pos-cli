<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/BantosBen/pos-cli">
    <img src="https://jengaschool.com/wp-content/uploads/2020/08/JENGA-School-Head.png" alt="Logo" width="80" height="80">
  </a>

<h1 align="center">POS-CLI PROJECT DOCUMENTATION</h1>

</div>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Main Page][product-screenshot]](https://github.com/BantosBen/pos-cli)

In its most basic form, POS-CLI is a point of sale terminal written in Python. The program revolves around three primary aspects: the customers, the items, and the acquisitions made by the customers. Python is used to create the system, which begins with a primary menu, obtains the user's selection from the menu, and then proceeds to run the subprogram that is connected with the menu. The information is kept in a file formatted in JSON. Additionally, the system is equipped with input validation, in addition to mail message for the customer's receipt of their purchase.
The Model-View-Controller (MVC) architecture was used when constructing the project structure of the code. This makes it possible for the system to have a codebase that is easily manageable, readable, and maintained.


### Functionalities
  #### Customer Module
    * Add new customer
    * Update customer details
    * Remove customer from the system
    * Search for customer
    * Validate user input
  #### Product Module
    * Add new product
    * Update product details
    * Remove product from the system
    * Search for product
  #### Puchase Module
    * Make a new order
    * Generate purchase report for a customer
    * View specific order details
    * Send receipt to customer via email


### Built With

* [![Python][Python]][python-url]
* [![JSON][JSON]][json-url]


### Code Architecture

[![Code Architecture][mvc]](https://github.com/BantosBen/pos-cli)

The Model-View-Controller (MVC) architecture was used when constructing the project structure of the code. This makes it possible for the system to have a codebase that is easily manageable, readable, and maintained.

<!-- GETTING STARTED -->
## Getting Started

It won't take you long to have the project running on your computer. The procedures needed to set up the project locally are outlined below.

### Prerequisites

You must first have Python3+ installed on your computer.You may look up this [guide](https://www.python.org/about/gettingstarted/) that will show you how to install Python on your computer.

### Installation

After determining that all of the prerequisites have been met, you are free to move forward with the project's acquisition.

Clone the repo
   ```sh
   git clone https://github.com/BantosBen/pos-cli.git
   ```
With the project successfully cloned to you computer, navigate into the project root folder and start cmd/terminal. Execute the folloeing command to start the project
   ```sh
   python main.py
   ```


<!-- CONTACT -->
## Developer Contact

Angatia Bensons - [@bensonetia](https://twitter.com/bensonetia) - angatiabenson1@gmail.com

Project Link: [https://github.com/BantosBen/pos-cli](https://github.com/BantosBen/pos-cli)



<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshot.PNG
[mvc]: images/mvc.PNG
[python]: https://img.shields.io/badge/python-356C9B?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/
[json]: https://img.shields.io/badge/Json-ADADAD?style=for-the-badge&logo=json&logoColor=61DAFB
[json-url]: https://json.org/

