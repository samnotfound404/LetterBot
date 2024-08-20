# Letter Generation Bot

This project is a Django-based application that enables users to create and receive customized letters via WhatsApp using Twilio's messaging API. The bot interacts with users through a series of prompts to gather necessary details for generating a PDF letter, which is then sent back to the user.

## Demo Video



https://github.com/user-attachments/assets/ec902140-aeed-4430-bda2-7420ff2a141e


*Note: The above is a short demonstration of how the Letter Generation Bot works.*
## Features

- **Interactive Letter Creation**: Users can create a letter by responding to a series of prompts via WhatsApp.
- **PDF Generation**: Converts the collected information into a well-formatted PDF letter.
- **Session Management**: Tracks user progress in letter creation across multiple interactions.
- **History Retrieval**: Users can request previous letters generated in their session.
- **Twilio Integration**: Sends and receives messages via the Twilio WhatsApp API.

## Installation

### Prerequisites

- Python 3.x
- Django
- Twilio Account
- wkhtmltopdf (for PDF generation)

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/letter-generation-bot.git
    cd letter-generation-bot
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Django settings:**

    - Update the `settings.py` file with your database configurations, Twilio credentials, and other settings like `MEDIA_ROOT` and `MEDIA_URL`.
    - Ensure `wkhtmltopdf` is correctly installed and its path is specified in the `letter()` function.

4. **Migrate the database:**

    ```bash
    python manage.py migrate
    ```

5. **Run the server:**

    ```bash
    python manage.py runserver
    ```

6. **Setup Twilio Webhook:**

    - In your Twilio console, set up a webhook for incoming messages pointing to your server's `/process_letter_request/` endpoint.

## Usage

1. **Starting a Conversation:**
   - Users start by sending "Hi" to the bot on WhatsApp.

2. **Step-by-Step Letter Creation:**
   - The bot will ask the user to provide various details such as the header, body, company name, etc.
   - Once all details are provided, a PDF letter is generated and sent back to the user.

3. **Retrieving Previous Letters:**
   - Users can type "older" to retrieve their last generated letter.


