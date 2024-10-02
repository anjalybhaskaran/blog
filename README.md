 Django Blog Application

A simple blog application built with Django.

## Project Overview
This blog application allows users to create accounts, write blog posts, and interact with content through comments and likes. It features a clean and responsive design.

### Features
- User authentication and profile management.
- Blog post creation, updating, and deletion.
- REST API for blog posts and user interaction.

### API Documentation

The API (or view-based routing) supports the following endpoints:

| Method | Endpoint                     | Description                     |
|--------|------------------------------|---------------------------------|
| GET    | /post/                        | List all blog posts (home page) |
| GET    | /post/<int:pk>/               | Retrieve a single blog post     |
| POST   | /newpost/                     | Create a new blog post          |
| PUT    | /post/<int:pk>/edit/          | Update an existing blog post    |
| DELETE | /post/<int:pk>/delete/        | Delete a blog post              |

