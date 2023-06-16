# Home Assistant "Fetch latest file" Custom Component

This custom component for Home Assistant allows you to fetch the latest files (such as camera screenshots and video events) from a specified directory. It was specifically designed for use with Reolink cameras and their integrations but can be easily adapted for a variety of other use cases.

## Installation

1. Copy the `fetch_latest_file` folder into your `custom_components` folder within your Home Assistant configuration directory.
2. Add the following to your `configuration.yaml`:

```yaml
fetch_latest_file:
```

## Usage

Once you've set up the custom component in your Home Assistant instance, you can call it using the service `files.fetch` with the following parameters:

- `directory`: The directory to search for files. *(Required)*
- `filename`: The start of the file name to search for. *(Required)*
- `extension`: The file extension(s) to search for. *(Optional)*

Here's an example of how to call this service:

```yaml
service: files.fetch
data:
  directory: "/path/to/your/directory"
  filename: "cam1"
  extension: ["jpg", "mp4"]
```

This will search for the latest `.jpg` and `.mp4` files that start with "cam1" in the specified directory. The result is then stored in a state which you can access in your automations, scripts, or templates.

## Use Case

The main use case for this component is in a home security setup with Reolink cameras. Whenever an event is triggered, Home Assistant fetches the relevant files and can post them to a specific Discord channel. This provides a streamlined way to access important security footage as soon as it is needed.

## Further Uses

This component can also be used in many other scenarios, such as:

- Fetching the latest screenshot from a home automation event
- Retrieving the latest log files for debugging purposes

This component is highly flexible and can be adapted to suit a variety of needs within your Home Assistant setup.

## Support

Feel free to [open an issue](https://github.com/bexem/Fetch-Lastest-file-HA-Custom-Component/issues) for any problems or feature requests.
