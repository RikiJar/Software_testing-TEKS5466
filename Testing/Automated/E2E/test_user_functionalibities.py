import re
import random
from playwright.sync_api import Page, expect

# Generate a random number to ensure unique usernames and passwords for each test run as there is no user deletion functionality
random_number = random.randint(1000, 9999)

def test_register(page: Page):
    page.goto("http://localhost")

    # Verify that the front page is displayed
    expect(page.get_by_role("heading", name="Welcome to Todo Manager")).to_be_visible()

    # Click the "To registration" button
    page.get_by_role("button", name="To Registration").click()

    # Verify that the registration page is displayed
    expect(page.get_by_role("heading", name="Register an account")).to_be_visible()

    # Fill in the registration form
    # Use a unique username for each test run
    page.get_by_label("Username").fill("test1" + str(random_number))
    
    # Use a unique password for each test run
    page.get_by_label("Password").fill("test_password" + str(random_number))

    page.get_by_role("button", name="Register").click()

    # Verify that the user is redirected to the main page after registration
    expect(page.get_by_role("heading", name="My todo lists")).to_be_visible()

def test_login_logout(page: Page):
    page.goto("http://localhost")

    # Verify that the front page is displayed
    expect(page.get_by_role("heading", name="Welcome to Todo Manager")).to_be_visible()

    # Fill username and password to log in
    page.get_by_label("Username").fill("test1" + str(random_number))
    page.get_by_label("Password").fill("test_password" + str(random_number))

    # Login and verify that user has logged in successfully
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="My todo lists")).to_be_visible()

    # Test logout functionality
    page.locator('text=Logout').click()

    # Verify that the user is redirected to the welcome page after logout
    expect(page.get_by_role("heading", name="Welcome to Todo Manager")).to_be_visible()

def test_create_delete_todo_list(page: Page):
    page.goto("http://localhost")

    # Verify that the front page is displayed
    expect(page.get_by_role("heading", name="Welcome to Todo Manager")).to_be_visible()

    # Fill username and password to log in
    page.get_by_label("Username").fill("test1" + str(random_number))
    page.get_by_label("Password").fill("test_password" + str(random_number))

    # Login and verify that user has logged in successfully
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="My todo lists")).to_be_visible()

    # Create a new todo list
    todo_name = str(random.randint(1, 9999))
    page.get_by_role("button", name="New todo list").click()
    page.get_by_label("Name").fill("Test Todo List" + todo_name)
    page.get_by_label("Description").fill("Test" + todo_name)
    page.get_by_role("button", name="Create").click()

    # Verify that the new todo list is created and visible
    expect(page.get_by_text("Test" + todo_name)).to_be_visible()

    # Delete the created todo list
    todo_row = page.locator("div.flex.flex-grow").filter(
        has=page.locator(f"text={todo_name}")
    )

    todo_row.locator(
        'button[icon="fluent:delete-20-regular"]'
    ).click()

    # Verify that the todo list is deleted
    expect(page.get_by_text("Test" + todo_name)).not_to_be_visible()