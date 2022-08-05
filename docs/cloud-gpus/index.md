---
template: cloud-gpus.html
hide:
    - toc
    - navigation
description: Detailed comparison table of all cloud GPU providers.
---

# Cloud GPUs


## Cloud Comparison

We have assembled cloud GPU vendor pricing all in one table, sortable and filterable to your liking!

Please make pull requests to the source files [cloud-gpus.csv](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/cloud-gpus.csv) and [gpus.csv](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/gpus.csv).

<div id="cloud-gpus-table"></div>

## GPUs

Below are the TFLOPs of the different GPUs available from cloud providers.

<div id="gpus-table"></div>

<small>
    Author: [Sergey Karayev](https://twitter.com/sergeykarayev)
</small>

<script>
function csvToArray(str, delimiter = ",") {
  // From https://sebhastian.com/javascript-csv-to-array/
  const headers = str.slice(0, str.indexOf("\n")).split(delimiter);
  const rows = str.slice(str.indexOf("\n") + 1).split("\n");
  const arr = rows.map(function (row) {
    const values = row.split(delimiter);
    const el = headers.reduce(function (object, header, index) {
      object[header] = values[index];
      return object;
    }, {});
    return el;
  });
  return arr;
}

fetch("./cloud-gpus.csv").then((res) => res.text()).then((text) => {
  const data = csvToArray(text);
  const cloud = new Handsontable(document.getElementById('cloud-gpus-table'), {
    data: data,
    licenseKey: "non-commercial-and-evaluation",
    colHeaders: Object.keys(data[0]),
    dropdownMenu: true,
    multiColumnSorting: true,
    filters: true,
    width: 'auto',
    height: 'auto',
    hiddenColumns: true,
    manualColumnResize: true,
    readOnly: true,
  });
});
fetch("./gpus.csv").then((res) => res.text()).then((text) => {
  const data = csvToArray(text);
  const cloud = new Handsontable(document.getElementById('gpus-table'), {
    data: data,
    licenseKey: "non-commercial-and-evaluation",
    colHeaders: Object.keys(data[0]),
    // dropdownMenu: true,
    // multiColumnSorting: true,
    // filters: true,
    width: 'auto',
    height: 'auto',
    hiddenColumns: true,
    manualColumnResize: true,
    readOnly: true,
  });
});
</script>
