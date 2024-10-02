 Django Blog Application

A simple blog application built with Django.

## Project Overview
This blog application allows users to create accounts, write blog posts, and interact with content through comments and likes. It features a clean and responsive design.

### Features
- User authentication and profile management.
- Blog post creation, updating, and deletion.
- REST API for blog posts and user interaction.

### API Documentation

The API supports the following endpoints:

| Method | Endpoint           | Description                     |
|--------|--------------------|---------------------------------|
| GET    | /api/posts/         | List all blog posts             |
| GET    | /api/posts/<id>/    | Retrieve a single blog post     |
| POST   | /api/posts/         | Create a new blog post          |
| PUT    | /api/posts/<id>/    | Update an existing blog post    |
| DELETE | /api/posts/<id>/    | Delete a blog post              |
