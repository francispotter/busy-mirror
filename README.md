# Tiger

A command-line task and plan management tool.

## Introduction

Tiger is a system for keeping track of tasks. Some of the guiding philosophies:

- Everything is based on a POSIX command line interface, making it easy to use from the terminal prompt on Linux and MacOS systems
- Data is stored in easily edited files, so if the tool doesn't do something you want, you can just edit the files
- There's an interactive option so you don't have to remember commands

## Commands

The main command is `tiger` (typically shortened with an alias to `ti`).

When called without any arguments, the command returns the current task.

Otherwise, the first positional argument is a command, which is one of the following.

| **Command** | **Shortened** |  **Description** |                                    **Designate tasks?** | **Default** |
| --- | ---| --- | -:- |
| `list` | `li` | List tasks in order, with sequence numbers                          | YES | All current tasks |
| `defer` | `de` | Push a task to a later date                                        | YES | Active task |
| `manage` | `ma` | Pull up the current list of tasks (today or earlier) in an editor | -   | All current tasks |
| `complete` | `co` | Complete the current task and do the followon thing             | YES | Active task |
| `start` | `st` | Set the `TIGER_ROOT` environment variable                          | -   | - |
| `drop` | `dr` | Drop a task to the bottom of the order                              | YES | Active task |
| `pop` | `po` | Pop a task to the top of the order                                   | YES | None |
| `add` | `ad` | Add a new task                                                       | -   | - |
| `delete` | `de` | Delete a task, without marking it complete                        | YES | Active task |
| `edit` | `ed` | Edit task                                                           | YES | Active task |


## Designating tasks

For some commands, it's possible to designate tasks to be acted upon. Desgnating tasks is always optional, although in the case of the `pop` command, nothing will happen if no tasks are designated.

Tasks are identified by number, which is the line number of that task within the list of tasks.

`tiger list` lists all the tasks

`tiger list 5` shows only task number 5

`tiger list 3-7` shows tasks 3-7

`tiger list 3-` show tasks 3 through the end

`tiger list 3 5 7 9` shows the tasks designated

_some way to indicate the last task?_

## Command line options

| **Option** | **Short** | **Description** |
| --- | --- | ---|
| `--help`     | `-h` | Describes usage of the command |
| `--root`     | `-r` | Defines the root for only this command |
| `--plan`     | `-p` | Include tasks that are scheduled for a future date |
| `--current`  | `-c` | Include current tasks - tasks for today or earlier |
| `--multiple` | `-m` | Handle more than one task (only for `add`) |
| `--then`     | ??   | Do another command after completing the first command |
| `--task`     | `-t` | Provide the task description (only for `new`) |


## Deferral

Deferral is about scheduling a task to reappear on the task list on a future date. To defer a task, you have to designate the date using the `--to` or `--for` option (they are interchangable). Some options:

- `1 day` or `1d` Tomorrow (the default) - can also write `tomorrow`
- `2 days` or `2d` The day after tomorrow
- `2018-10-28` A specific date in `YYYY-MM-DD` format
- `10-28` A specific date in `MM-DD` format; assumes the next version of that date
- `10/28` Alternative to the above
- `tue` The next of this day of the week; could be long or short form, caps insensitive
- `the 28th` Arbitrary day of the month; the word `the` is required but the letters after the number are arbitrary - just requires some letters
- `4 fridays` Not the coming Friday, but the 4th friday after today

Example:

```
tiger defer 4-6 --for 4 days
```

## The `then` option

The `--then` option is most useful with the `add` command. For example, the following command allows you to pop the new tasks to the top.

`tiger add --multiple --then pop`

The `--then` option requires an argment, which must be one of:

- pop
- drop
- defer
- complete


## Followons

Followons are entered into the task with the `-->` indicator. They designate what to do when the task is completed.

A followon is a derral that will be automatically applied after completion. This allows repetition of tasks on a schedule.

Example:

```
Go to the store --> friday
```



## Adding tasks

| **Where** | **One** | **Multiple** |
| --- | --- | ---|
| Bottom of current | `add` | `add --multiple` |
| Top of current | `add --pop` | `add --multiple --pop` |
| Deferred | `add --defer` | `add --multiple --defer` |

Note that if you add multiple with pop, they stay in order.

```
tiger add --multiple --pop
Go to the store
Go to the bank
```

Then:

```
tiger list 1-2
    1 Go to the store
    2 Go to the bank
```

Task descriptions always come from stdin. To read from a file, try:

```
cat list-of-tasks.txt | tiger add --multiple
```

## Data storage

Tiger requires a "root", which is the directory containing the two data files:

`todo.txt` - current tasks
`plan.txt` - future tasks, with dates
`done.txt` - log of completed tasks

Technically, they are pipe-delimited data files, though `todo.txt` only has one field.

How to tell tiger its root (in order)

- The `--root` option
- The `TIGER_ROOT` environment variable
- Otherwise, `~/.tiger` which will be generated as needed


The "root" setup allows you to have separate task queues for separate projects.

## Notes

- Need a way to add a task to another queue.

## Architecture

- Domain model (item/queue/etc)
- Operations layer: pure python
- Command layer: handles commands, options, and files - with output to text
