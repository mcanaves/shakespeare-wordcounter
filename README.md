# Shakespeare Word Counter

[![Build Status](https://travis-ci.com/mcanaves/shakespeare-wordcounter.svg?branch=master)](https://travis-ci.com/mcanaves/shakespeare-wordcounter)

Little project that tells you how many times Shakespeare use every word in three of his masterpieces. These books are:

- King Lear
- Othello
- Romeo and Juliet

## Prerequisites

You’ll need at least Docker 1.17.

If you don’t already have it installed, follow the instructions for your OS:

- On Mac OS X, you’ll need [Docker for Mac](https://docs.docker.com/docker-for-mac/)
- On Windows, you’ll need [Docker for Windows](https://docs.docker.com/docker-for-windows/)
- On Linux, you’ll need [docker-engine](https://docs.docker.com/engine/installation/)

## Usage

Simply run the following script:

**Note:** *docker image must be built before try to run this script.*

```bash
./scripts/run
```

And once the execution of the script is finished you will be able to see a file called `result.csv` that contains the word count.

## Development

To work with this codebase you'll want to clone the repository and build the docker image:

```bash
git clone git@github.com:mcanaves/shakespeare-wordcounter
cd shakespeare-wordcounter
./scripts/setup
```

To lint the code and run the tests run the following scripts:

**Note:** *docker image must be built before try to run any of these scripts*

```bash
./scripts/lint
./scripts/test
```
