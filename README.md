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
