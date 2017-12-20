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

    cd find-job/
    python3 -m venv venv_name
    source venv_name/bin/activate
    pip install -r requirements.txt

Make sure MongoDB is running on your system, you can check its status by typing:

    sudo service mongod status

If it's not running, fire it up:

    sudo service mongod start

Start crawling using scrapy:

    cd find_job/
    python crawl.py -k python # Replace 'python' to whatever keyword you want.

It will create a new database named **find_job** in MongoDB, all found jobs will be stored into **jobs** collection.

    # jobs collection
    {
        "_id": ObjectId(),
        "name": Job's title,
        "location" Job's location,
        "company": Offer's company,
        "salary": Salary range,
        "date": Post date,
        "url": Link to post
    }

Export data in JSON format

    mongoexport -d find_job -c jobs -o jobs.json

See [Official docs](https://docs.mongodb.com/manual/reference/program/mongoexport/) for more export usage.

## Built With
* [Scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
