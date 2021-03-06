# Inu

> A Discord bot for the Bulldog Computer Club using [discord.py](https://github.com/Rapptz/discord.py).

## Installation

1. Clone the repository locally:
   ```bash
   $ git clone https://github.com/Bulldog-Computer-Club/inu
   ```
2. Navigate to the newly created folder:
   ```bash
   $ cd inu
   ```
3. Copy `.env.example` to `.env` and fill it out with the necessary configuration values.

After this, there are two possibilities:

### Running standalone

> **Note:** Running standalone requires more work in general, but is beneficial for fast iteration when developing.

1. Set up [Poetry](https://python-poetry.org/), which is used for package management and build control.
2. Install all dependencies:
   ```bash
   $ poetry install
   ```
3. Run the `bot.py` file:
   ```bash
   $ poetry run python bot.py
   ```

## Running via Docker

> **Note:** Running via Docker is recommended for production instances, but may have a relatively low start-up speed compared to running standalone.

1. Ensure that [Docker](https://www.docker.com/) is installed on your system.
2. Use Compose to start the bot service:
   ```bash
   $ docker-compose up
   # or, if developing
   $ docker-compose up --build bot
   ```

If developing, it is recommended to comment out the restart policy in the Compose file.

## Contributing

Thank you for considering contributing to Inu; bug-fixes and new features are always appreciated. If working on a major feature, it may be prudent to open an issue to discuss design and implementation prior to diving in to avoid any surprises down the line.

### Development Tools

[Black](https://github.com/psf/black) is used for code formatting and [Flake8](https://flake8.pycqa.org/en/latest/) for style enforcement. Having these tools and relevant editor integrations installed will be a major boon for development.

## License

Inu is licensed under the MIT license. It is maintained by the organizers of the Bulldog Computer Club, with help from club members.
