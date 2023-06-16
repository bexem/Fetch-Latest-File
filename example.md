# Home Assistant Automation and Script Guide

This guide describes an automation and script setup in a home automation context, particularly involving CCTV cameras and Home Assistant.

## Automation

The automation triggers when either the front camera (`binary_sensor.front_person`) or the doorbell camera (`binary_sensor.doorbell_person`) detects motion. Based on the source of the trigger, it performs several actions including text-to-speech (TTS) announcements and notifications.

```yaml
trigger:
  - platform: state
    entity_id:
      - binary_sensor.front_person
    to: "on"
    from: "off"
    id: front
  - platform: state
    entity_id:
      - binary_sensor.doorbell_person
    to: "on"
    from: "off"
    id: doorbell
[...]
condition:
[...]
action:
  - choose:
      - conditions:
          - condition: trigger
            id: front
        sequence:
            [...]
          - parallel:
              [...]
              - service: script.cctv_camera_notifications
                data:
                  message: Person detected by the front camera
                  title: Person detected - Front
                  camera: camera.front_sub
              - service: script.notification_cctv_discord
                data:
                  camera: camera.front_sub
            alias: Notifications
      - conditions:
          - condition: trigger
            id: doorbell
        sequence:
            [...]
          - parallel:
              [...]
              - service: script.notification_cctv_discord
                data:
                  camera: camera.doorbell_sub
            alias: Notifications
[...]
```

## Script

The script, which is triggered by the automation, sends notifications to a Discord server, attaching the latest image and video from the CCTV feed. At the start of the script, several variables are set, including `folder` which specifies the directory to fetch files from, and `nvr_name` which determines the name of the camera channel set by the NVR.

```yaml
sequence:
      folder: /media/cctv/reolink/
      channel: |
        {% if 'doorbell' in camera %}
          REDACTED_DISCORD_CHANNEL
        {% elif 'front' in camera %}
          REDACTED_DISCORD_CHANNEL
        {% else %}
          0
        {% endif %}
      file_name: |
        {% if 'doorbell' in camera %}
          doorbell
        {% elif 'front' in camera %}
          front
        {% else %}
          0
        {% endif %}
      nvr_name: |
        {% if 'doorbell' in camera %}
          NVR_00
        {% elif 'front' in camera %}
          NVR_01
        {% else %}
          0
        {% endif %}
  - service: latest.fetch
    data:
      Directory: "{{folder}}"
      FileName: "{{nvr_name}}"
      Extension:
        - jpeg
        - mp4
  - parallel:
      - if:
          - condition: template
            value_template: "{% if 'video' in states.latest.file.attributes %}{{ true }}{% else %}{{ false }}{% endif %}"
        then:
          - service: notify.discord
            data_template:
              target: "{{channel}}"
              message: Video
              data:
                images:
                  - "{{ states.latest.file.attributes.video }}"
    [...]
```