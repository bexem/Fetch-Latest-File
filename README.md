# Home Assistant "Fetch latest file" Custom Component

This custom component for Home Assistant allows you to fetch the latest files (such as camera screenshots and video events) from a specified directory. It was specifically designed for use with Reolink cameras and their integrations but can be easily adapted for a variety of other use cases.

## Installation

1. Copy the `fetch_latest_file` folder into your `custom_components` folder within your Home Assistant configuration directory.
1. Or install it via [![hacs_badge](https://my.home-assistant.io/redirect/hacs_repository/?owner=bexem&repository=https%3A%2F%2Fgithub.com%2Fbexem%2FFetch-Lastest-file-HA-Custom-Component&category=integrations) using the HACS custom repositories:
    1. Go to any of the sections (integrations, frontend, automation).
    2. Click on the 3 dots in the top right corner.
    3. Select "Custom repositories"
    4. Add the [URL](https://github.com/bexem/Fetch-Lastest-file-HA-Custom-Component) to the repository.
    5. Select the integration category.
    6. Click the "ADD" button.
2. Add the following to your `configuration.yaml`:

```yaml
fetch_latest_file:
```

## Usage

Once you've set up the custom component in your Home Assistant instance, you can call it using the service `latest.fetch` with the following parameters:

- `directory`: The directory to search for files. *(Required)*
- `filename`: The start of the file name to search for. *(Required)*
- `extension`: The file extension(s) to search for. *(Optional)*

Here's an example of how to call this service:

```yaml
service: latest.fetch
data:
  directory: "/path/to/your/directory"
  filename: "cam1"
  extension: ["jpg", "mp4"]
```

This will search for the latest `.jpg` and `.mp4` files that start with "cam1" in the specified directory. The result is then stored in a state which you can access in your automations, scripts, or templates.

## Use Case

The main use case for this component is in a home security setup with Reolink cameras. Whenever an event is triggered, Home Assistant fetches the relevant files and can post them to a specific Discord channel. This provides a streamlined way to access important security footage as soon as it is needed.

### [See My example](https://github.com/bexem/Fetch-Lastest-file-HA-Custom-Component/wiki/Example)

## Further Uses

This component can also be used in many other scenarios, such as:

- Fetching the latest screenshot from a home automation event
- Retrieving the latest log files for debugging purposes

This component is highly flexible and can be adapted to suit a variety of needs within your Home Assistant setup.

## Support

Feel free to [open an issue](https://github.com/bexem/Fetch-Lastest-file-HA-Custom-Component/issues) for any problems or feature requests.
