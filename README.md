# WhatsApp Auto Response Bot
![image](https://github.com/user-attachments/assets/76ab1faa-8ff8-4cac-920a-21b9823bd8b1)


![WhatsApp Auto Response Bot Logo](https://via.placeholder.com/150)  <!-- Replace with your project logo or image URL -->

An automated WhatsApp bot that responds to incoming messages based on pre-configured patterns. This bot is designed to save time and automate basic responses to common messages on WhatsApp.

---

## 🚀 Features
- **Automated Responses:** Automatically replies to messages based on specific keywords.
- **Customizable:** You can configure custom responses for various messages like "Good Morning," "Happy New Year," and more.
- **WhatsApp Integration:** Direct integration with WhatsApp Web using Python and PyAutoGUI for automation.
- **Easy Setup:** Simple installation and usage instructions.

---

## 🛠️ Installation

### Prerequisites
- [Python 3.x](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [pyperclip](https://pyperclip.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

### Steps to Install
1. Clone the repository:
    ```bash
    git clone https://github.com/ghdbashen/whatsapp-auto-response-bot.git
    ```

2. Navigate into the project directory:
    ```bash
    cd whatsapp-auto-response-bot
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the bot (ensure WhatsApp Web is open in your browser):
    ```bash
    python wa.py
    ```

---

## 🔧 Usage

Once the bot is running, it will continuously monitor incoming WhatsApp messages and reply based on the keywords found in the message.

### How it works:
- The bot checks for new messages.
- If the message contains specific keywords like "Good Morning," it will respond with a predefined message like: `"Good Morning! Have a great day."`
- You can modify or add new responses by editing the `process_response` function in the code.

---

## 📄 Customizing Responses

To customize the responses:
1. Open the `wa.py` file.
2. Modify the `process_response()` function by adding more conditions for different messages.

### Example:
```python
if "happy birthday" in str(message).lower():
    return "Happy Birthday! 🎉🎂 Wishing you a wonderful year ahead! - Bot"

