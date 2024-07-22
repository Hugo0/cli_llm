# cli_llm

A little tool to use Large Language Models in the cli.

idk how to use Linux sometimes and this is useful :)

## Usage:

```bash
hugo@hugo-fw:~$ llm how to cat only the last 20 lines of a file?
You can use the `tail` command to display the last lines of a file. To see only the last 20 lines of a file, you can run the following command:

tail -n 20 filename

Replace `filename` with the actual name of the file you want to view. This command will display the last 20 lines of the file on the terminal.
hugo@hugo-fw:~$ 
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cli_llm.git
   cd cli_llm
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root:
     ```bash
     touch .env
     ```
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

5. Add the following function to your `~/.bashrc` file:
   ```bash
   llm() {
       source ~/path/to/cli_llm/venv/bin/activate
       python ~/path/to/cli_llm/cli_llm.py "$@"
       deactivate
   }
   ```
   Replace `~/path/to/cli_llm` with the actual path where you cloned the repository.

6. Reload your `.bashrc`:
   ```bash
   source ~/.bashrc
   ```

Now you can use the `llm` command from anywhere in your terminal!