# About

This is just another general bot repository trying to incorperate a bunch of features into **one** functioning bot, except for moderation. Because moderation is hard and there are already a bunch of great bots for that.

If you have any ideas for this project, you can fork it and add them to the [todo.md](./todo.md) or create an [issue](https://github.com/BOEM25/The-Bot/issues) with enhancement lable. Optionally you can code these ideas yourself and make a pull request :).

## Config file

```json
{
    "token": "token",
    "bot_name": "Bot",
    "description": "bot",
    "settings": {
        "some_setting": false, <-- placeholder
        "log_level": "CRITICAL"
    }
}
```

### Token

`"token":` bot token from [discord developers](https://discord.com/developers) panel.

### Bot name

`"bot_name":` whatever bot name you want. Used in some messages send by bot, will not change the name set in the developers panel.

### Description

`"description":` a message describing the bots purpose and some explaination. This message is send after using the /description command.

### Settings

#### Some value

`"some_value":` Placeholder

#### Logging Levels

`"log_level:"` how indepth the logging is.

- CRITICAL
- ERROR
- WARNING
- INFO
- DEBUG
- NOTSET
