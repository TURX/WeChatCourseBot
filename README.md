# WeChat Robot for Online Courses

copyright by &copy; TURX, licensed by GPL v3.

## Functions

- Auto repeat others' one-word message within several repetitions. (1.0)
- Auto respond when being mentioned or at by others (1.0).
- Support multiple groups with whitelist. (1.0)
- Support JSON configuration. (1.0)
- Auto join Zoom meeting (support seperated messages started by conference number and password). (1.0)

## Dependencies

- itchat
- pip
- Python 3

## Usage

You can go to [releases](https://github.com/TURX/QQCourseBot/releases) to download a repo or clone the master branch.

```sh
cd /path/to/repo # change to exact value

pip3 install itchat # install dependencies

python3 main.py # run the robot
```

## Configuration

The json files will be generated if not exist in first run:

- personal.config.json:

Fill in your lowercased real name.

```json
testname
```

- response.config.json:

Set responses to send when being mentioned.

```json
[
    "My internet is poor.",
    "I am restarting my router.",
    "My device has no battery now."
]
```

- whitelist.config.json:

Use the following configuration with whitelisted WeChat group names (no whitelisted group has same name with others):

```json
[
    "A's Group Chat",
    "B's Class"
]
```
