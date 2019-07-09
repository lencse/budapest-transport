# Budapest public transport stops

A script to analyze the distance between stops of public transport in Budapest 

## Prerequisites

* Python 3
* Pipenv

## Starting

```bash
git clone git@github.com:lencse/budapest-transport.git
cd budapest-transport
pipenv shell
```

## Usage

Show the greatest distance between two stops with the same name
```bash
./budapest report
```

List with numbers
```bash
./budapest report | cat -n | less
```

Open the map for two most far stops with a given name in the browser
```bash
./budapest map "Kelenföld vasútállomás M"
```
![Map screenshot](doc/map-screenshot.png)

Open map for multiple stops in the browser
```bash
./budapest map "Kelenföld vasútállomás M" "Móricz Zsigmond körtér M" "Papírgyár"
```

Show the GPS data for the stops
```bash
./budapest data
```

Open the map for stops in interval [100, 110]
```bash
./budapest data | awk '100 <= NR && NR <= 110' | cut -f1 | tr '\n' '\0' | xargs -0 ./budapest map
```

## Data source

On the first run, the script downloads the data provided by
[BKK](https://bkk.hu/tomegkozlekedes/fejlesztoknek/)
