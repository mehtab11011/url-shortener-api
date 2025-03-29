## Project Review: URL Shortener REST API

### Overview
The **URL Shortener REST API** is a web service designed to shorten long URLs, retrieve original URLs, update or delete links, and track access counts. This project was developed for an assignment from **Innovexal Company** and is built using **Django** and **Django Rest Framework (DRF)**.

### Key Features:
- **Shorten URL**: Converts long URLs into shorter, easily shareable links.
- **Retrieve Original URL**: Redirects users to the original URL when they visit the shortened link, while tracking the access count.
- **Update and Delete**: Allows users to update or delete shortened URLs as needed.
- **Access Tracking**: Tracks the number of times each shortened URL is accessed.

### Tech Stack:
- **Python**: Backend development.
- **Django & Django Rest Framework (DRF)**: Building the API.
- **SQLite**: Database management.

### Challenges:
- **Unique URL Generation**: Ensuring the uniqueness of shortened URLs was challenging, but it was effectively handled by a random string generator.
- **Data Integrity**: Maintaining accurate access counts under heavy traffic was tricky, which was managed using Django’s ORM.
- **API Design**: Designing a smooth and error-free API, especially to handle non-existent URLs, posed a challenge.

### Future Enhancements:
- **Custom URLs**: Allow users to create their own custom shortened URLs.
- **Analytics Dashboard**: Add a feature to display access data for each URL.
- **User Authentication**: Enable secure user management of shortened URLs.
- **Rate Limiting**: Implement rate-limiting to prevent abuse and enhance API security.

### Conclusion:
The **URL Shortener REST API** project offers a simple yet effective solution for shortening and managing URLs. It successfully provides essential features such as URL shortening, updating, deletion, and access tracking. Built with **Django** and **DRF**, the project is scalable and easy to extend. It can be enhanced with additional features based on user feedback.



# How to Run the Project

Follow these steps to run the **URL Shortener REST API** project locally on your machine:

### 1. **Clone the Repository**
First, clone the project repository to your local machine using the following command:
```bash
git clone https://github.com/your-username/url-shortener.git
2. Navigate to Project Directory
Once cloned, navigate into the project directory:

cd url-shortener
3. Create a Virtual Environment (Optional but Recommended)
It is recommended to use a virtual environment to manage dependencies. You can create one using the following command:
python -m venv venv
Activate the virtual environment:
For Windows:
venv\Scripts\activate
For macOS/Linux:
source venv/bin/activate

4. Install Dependencies
Install the required dependencies by running:

pip install -r requirements.txt
5. Setup Database
If the database has not been set up yet, you can run the following command to apply migrations:

python manage.py migrate
6. Run the Development Server
Start the development server by running:
python manage.py runserver
This will start the server at http://127.0.0.1:8000/.

7. Test the API
You can now test the API using a tool like Thunder Client or Postman. Here are the available API endpoints:

Shorten URL:

POST /shorten/

Request body (example):

{
  "Original_URL": "https://example.com"
}
Retrieve Original URL:

GET /return/{short_url}/

Example: GET http://127.0.0.1:8000/return/eAipBw/

Redirects to the original URL.

Update URL:

PUT /update/{short_url}/

Request body (example):

{
  "Original_URL": "https://new-url.com"
}
Delete URL:

DELETE /delete/{short_url}/

Access Count:

GET /count/{short_url}/

Returns the number of times the shortened URL has been accessed.

8. Shut Down the Server
Once done, you can stop the development server by pressing Ctrl+C in the terminal.





