<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./images/surf-spot-finder-logo-white.png">
    <source media="(prefers-color-scheme: light)" srcset="./images/surf-spot-finder-logo-black.png">
    <img src="./images/surf-spot-finder-logo-black.png" width="35%" alt="surf spot finder project logo"/>
  </picture>
</p>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[Documentation](https://mozilla-ai.github.io/surf-spot-finder/)
| [Getting Started](https://mozilla-ai.github.io/surf-spot-finder/getting-started)
| [Contributing](CONTRIBUTING.md)

</div>

# Surf Spot Finder

Surf Spot Finder helps you automatically identify the best surf spot for you, around a provided location, for a given date and within a specified driving distance. It leverages agent frameworks and LLMs to evaluate weather, surf, and travel data using open and extensible tool integrations.

## Quick-start

To use Surf Spot Finder, install the package and run via command line:

```bash
pip install -e .

surf-spot-finder --config <path/to/config.yaml>
```

You can also use the framework-free version:

```bash
surf-spot-finder-no-framework --location "Athens, Greece" --max_driving_hours 2 --date "2024-06-01-08" --model_id openai/gpt-4o
```

See [docs](https://mozilla-ai.github.io/surf-spot-finder/) or provided example configurations for more details.

## How it Works

The Surf Spot Finder:
- Uses configuration-driven agents (or a simplified agent-free mode) to:
  - Search for surfing spots in a geographic radius
  - Check forecast data (wind, wave) for chosen date
  - Optionally browse the web for surf spot reports
  - Score and recommend the best spot for your needs
- Can be extended with additional tools or evaluation logic via the agent configuration files

Supported agent frameworks: [smolagents](https://github.com/context-labs/smol-agents), [OpenAI](https://platform.openai.com/)

## Pre-requisites

- **System requirements:**
  - OS: Windows, macOS, or Linux
  - Python 3.11 or higher
  - Minimum RAM: ~2GB recommended
  - Disk space: Minimal

- **Dependencies:**
  - Listed in `pyproject.toml`, typically including: `any-agent[all]`, `fire`, `pydantic`, `pyyaml`, `litellm`, `geocoder`, `rich`

- **Optional:** For demo and docs use: `gradio`, `mkdocs`, etc.

## Troubleshooting

- Ensure all required Python dependencies are installed (`pip install -e .[demo,docs]` for extras)
- Some tools require API keys (for location or weather queries, or LLMs)
- Configuration can be customized via YAML or CLI flags; see [example configs](examples/) or `surf-spot-finder --help`.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! To get started, you can check out the [CONTRIBUTING.md](CONTRIBUTING.md) file.
