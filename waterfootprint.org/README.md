# Purpose

Use pandas script to filter the desired data from the original dataset.

# Dataset Information

- What: Blue/Green/Gray Water footprint of Crops by Country and sub regions
- Original dataset: https://waterfootprint.org/en/resources/waterstat/product-water-footprint-statistics/
- Transformed data : Filtered cleaned up data in folder `transformed_data`

## Sample usecase from this data

If a user wants to know water footprint of `Pistachios from Afghanistan`, we could infer following :

- m3/ton of blue/green/gray water usage in Afghanistan. Compare to GlobalAverage usage for that crop.
- show bar chart of Pistachios' blue water usage from Afghanistan compare to top 3 countries
- show bar chart of Pistachios' blue water vs a baseline crop like Wheat in Afghanistan

## Prereqs

- python 3 , pip

## To run a script

- Create Python Virtual Env
  ```
  $ python3 -m venv your/path/myenv
  $ source your/path/myenv/bin/activate
  $ pip install -r requirements.txt
  ```
- run a script:
  ```
  $ python3 {script_path}
  ```
