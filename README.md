# Find-job
A simple crawler to find jobs from several websites.
* INSIDE Job Board(https://jobs.inside.com.tw/)
* mit.jobs(https://mit.jobs/)

## Dependencies
* Python3+
* MongoDB

## Getting Started
### Installation
Clone this repository:

    git clone git@github.com:damnee562/find-job.git

Create virtualenv and install all requirements:

    cd find-job
    python3 -m venv venv_name
    source venv_name/bin/activate
    pip install -r requirements.txt

Make sure MongoDB is running on your system, you can check its status by typing:

    sudo service mongod status

If it's not running, fire it up:

    sudo service mongod start

Start crawling using scrapy:

    cd inside_jobs # or cd mit_jobs
    scrapy crawl jobs -a keyword=python # Replace 'python' to whatever keyword you want.

It will create a new database named **inside_jobs** or **mit_jobs** in MongoDB, all found jobs will be stored into **jobs** collection.

    {
        "_id": ObjectId(),
        "category": Job type,
        "salary": Salary range,
        "name": Job title,
        "location": Job location,
        "company": Job company,
        "url": Job link
    }

## Built With
* [Scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites.
