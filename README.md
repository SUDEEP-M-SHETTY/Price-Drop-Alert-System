### Price Drop Alert System

This Python script monitors the price of a product from Flipkart(an e-commerce website) and notifies the user when the price drops below a specified minimum.

#### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SUDEEP-M-SHETTY/price-drop-alert.git
   cd price-drop-alert
   ```

2. **Install dependencies:**
   Ensure you have Python 3.x installed on your system. Install required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary libraries:
   - `requests` for making HTTP requests
   - `beautifulsoup4` for parsing HTML content
   - `plyer` for sending system notifications

#### Usage

1. **Run the script:**
   ```bash
   python price_check.py
   ```

2. **Follow the prompts:**
   - Enter the complete URL of the product you want to monitor.
   - Enter the minimum price threshold. You will receive a notification when the price drops below this threshold.

3. **Notifications:**
   - **Linux:** Uses `notify-send` command for notifications. Ensure `notify-send` is installed (`sudo apt install libnotify-bin` on Debian/Ubuntu).
   - **macOS:** Uses AppleScript for displaying notifications.
   - **Windows:** Uses `plyer.notification` for displaying notifications.

#### Contributing

Contributions are welcome! Here's how you can contribute to this project:

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/SUDEEP-M-SHETTY/price-drop-alert.git
   cd price-drop-alert
   ```
3. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/new-feature
   ```
4. **Make changes** and test your changes thoroughly.
5. **Commit** your changes:
   ```bash
   git commit -am 'Add new feature'
   ```
6. **Push** to your branch:
   ```bash
   git push origin feature/new-feature
   ```
7. **Submit a pull request** on GitHub.

### Notes

- This script periodically checks the price of the product and notifies you if the price drops below your specified threshold.
- Ensure your system has appropriate permissions to display notifications (especially for macOS and Linux).
- Customize or extend the script as needed for additional functionality or specific use cases.

By following these steps, you can effectively use and contribute to this price drop alert system, enhancing its capabilities and usability over time.
