# Busy

A command-line task and plan management tool, for use from the terminal prompt on Linux and MacOS systems.

## Installation

```
pip3 install busy
```

## Generic queue management

The most general use of Busy is to track items in queues. The default queue is the `todo` queue. There are some basic commands that operate on all queues:

### The `add` command

Adds a new item to the bottom of the queue.

```
busy add "Donate to the busy project"
```

```
busy add "Office Space" --queue movies
```

If no item description is provided with the command, it will be read from stdin.

```
echo "Buy a tree" | busy add --queue christmas
```

The `add` command also takes an optional `--multiple` option which reads until EOF (_future feature_).

```
cat list-of-tasks.txt | busy add --multiple
```

### The `get` command

Get the top item in the queue, referred to as the "current" item. There are no options.

To get the top item in `todo`:

```
busy get
```

To get the top item in `movies`:

```
busy get --queue movies
```

### The `list` command

Lists the items in the queue in order with their sequence numbers.

```
busy add "Run"
busy add "Jump"
busy add "Sing"
busy list
```

Produces this output:

```
1  Run
2  Jump
3  Sing
```

The sequence numbers may be used in the `list`, `pop`, `drop`, `delete` and `manage` commands to designate specific tasks to be handled by those commands.

Note that the numbering starts with 1, and is not an ID -- the number of a item will change when the queue is modified. So always reference the most recent output from the `list` command.

Below are some examples of task designation using the `list` command, although the same syntax works with all the commands that handle designated tasks.

`busy list` lists all the tasks

`busy list 5` shows only task number 5

`busy list 3-7` shows tasks 3-7

`busy list 3-` show tasks 3 through the end

`busy list 3 5 7 9` shows the tasks designated

`busy list -` shows the last task

`busy list -4` is an error! Use `busy list 1-4` instead.

Note the result is always in the order the tasks appear in the queue, regardless of the order the criteria are provided.


### The `pop` command

Moves an item or a set of items to the top of the queue. The default is to move the bottom item to the top.

```
busy pop
busy list
```

Produces this output:

```
1  Sing
2  Run
3  Jump
```

Tasks may be designated for the `pop` command, in which case the designated tasks are moved to the top in the order they appear.

```
busy pop 2
busy list
```

```
1 Run
2 Sing
3 Jump
```

### The `drop` command

The opposite of `pop`. Move an item or a set of items to the bottom of the queue. The default is the top item.

### The `delete` command

Permanently deletes an item from the queue. The default is the top item.

| `manage`    | Edit tasks in an editor                                           | YES | All active tasks |

## The `manage` command

The `manage` command launches the user's default text editor to directly edit a queue or part of a queue.

Busy uses the `sensible-editor` command to select a text editor, which works with default Ubuntu Linux installations and might or might not work with other operating systems.

The default use of `manage` will edit the entire queue.

```
busy manage --queue movies
```

But it's also possible to designate tasks to be managed. The `manage` command does its best to replace the edited items in place in the list order. So if you `manage` the current project (in which all the tasks are at the top), then the edited tasks will still appear at the top. Even if you add tasks, they will be inserted after the last task in the managed set, not at the end of the list. But all the tasks brought up in the editor will be managed. So if you remove a task in the editor, it will be deleted and the others will be moved up to take its place.



## Introduction

Busy is a system for keeping track of tasks. Some of the guiding philosophies:

- There are "active" tasks, which is an ordered list of things to work on (also called "todos"), and there are "plans", which are things that have been deferred to a specific future date
- The "current" task is the top of the "active" task list, so it's the thing to do right now
- Everything is based on a POSIX command line interface, making it easy to
- Data is stored in easily edited files, so if the tool doesn't do something you want, you can just edit the files

## Commands

The main command is `busy`.

Otherwise, the first positional argument is a command, which is one of the following.

| **Command** | **Description** |                                    **Designate tasks?** | **Default** |
| --- | ---  | --- | --- |
| `get`       | Get the current task, no options                                  | -   | Current task       |
| `list`      | List active tasks (or plans, with an option) in order, with sequence numbers | YES | All active tasks |
| `add`       | Add a new active task                                                | -   | - |
| `drop`      | Drop a task to the bottom of the active order                       | YES | Current task |
| `pop`       | Pop a task or tasks to the top of the active order                   | YES | The last task on the active list |
| `delete`    | Delete a task                        | YES | Current task |
| `defer`     | Convert an active task into a plan for a specific later date       | YES | Current task |
| `activate`  | Make a plan or plans active, include a 'today' option           | YES - plans | - |
| `start`     | Starts work on a particular project (see below)                 | -   | - |
| `manage`    | Edit tasks in an editor                                           | YES | All active tasks |

### Task tags

Tasks can have tags, which are designated with space-separated hashtags in the task description, for example:

```
go to the supermarket #errands
```

Tags can be used in task designation, for example:

```
busy pop errands
```

A task can have no tags, one tag, or more than one tag.

`busy list admin` list all the tasks with the `#admin` hashtag somewhere in their description.

Task designation criteria are additive -- that is, a logical OR. So:

`busy list admin sales 3 4` will list all the admin tasks, sales tasks, and tasks 3 and 4.


## Command line options

| **Option** | **Description** |
| --- | ---|
| `--root`  | Defines the root for only this command |
| `--queue` | Designate which queue to use; default is `todo` |
| `--yes`   | Don't require confirmation of deletions |
| `--today` | Activate tasks for today or earlier (only for `activate`) |

## Deferral

Deferral is about scheduling a task to reappear on the task list on a future date. To defer a task, you have to designate the date using the `--to` or `--for` option (they are interchangable). Some options:

- `1 day` or `1d` Tomorrow (the default) - can also write `tomorrow`
- `2 days` or `2d` The day after tomorrow
- `2018-10-28` A specific date in `YYYY-MM-DD` format

Example:

```
busy defer 4-6 --for 4 days
```

## Projects and the `start` command

If a task has tags, the first tag is considered to be its "project" for the purposes of the `start` command.

The `start` command is used to start work on a project. If an argument is passed to the command, that's the chosen project. Otherwise the chosen project is the project of the current task. The command basically combines steps:

- Calls `activate --today` so the active task list is up-to-date
- Calls `manage` on the project, to edit the list of tasks for the project
- Calls `pop` on the project, so its tasks are at the top of the list

## Data storage

Tiger requires a "root", which is the directory containing the two data files:

- `todo.txt` - active tasks
- `plan.txt` - future tasks, with dates

Technically, they are pipe-delimited data files, though `todo.txt` only has one field.

How to tell busy its root (in order)

- The `--root` option
- The `BUSY_ROOT` environment variable
- Otherwise, `~/.busy` which will be generated as needed

The "root" setup allows you to have separate task queues for separate projects.

## Alternate lists

Some of the `busy` commands can be used on other lists. For example, you might have a shopping list called `shopping.txt` in the root directory. Just use the appropriate modifier for the following commands:

| **Command** | **Modifier** |
| --- | --- |
| `add`       | `to`         |
| `get`       | `from`       |
| `delete`    | `from`       |
| `list`      | `from`       |
| `pop`       | `in`         |
| `drop`      | `in`         |

Some examples:

```
add to movies
delete 3 from shopping
drop in friends
```

## Development

Although it requires Python 3.6.5 or higher, Busy is designed to function with the Python standard library without any additional pip modules.

However, we use coverage during unit testing, so:

```
pip3 install coverage
```

Then to run the test suite:

```
make test
```

Or to run test coverage:

```
make cover
```
